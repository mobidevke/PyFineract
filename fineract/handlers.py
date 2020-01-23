import datetime
import functools
import json
import textwrap
from typing import Dict, Union
from urllib.parse import urlparse

import requests
from requests import HTTPError
from requests.auth import HTTPBasicAuth

from fineract.exceptions import BadCredentialsException, ResourceNotFoundException, BadArgsException, FineractException


def indent(text, prefix):
    return textwrap.indent(text, prefix)


class RequestHandler:

    def __init__(self, username, password, base_url, tenant, timeout, per_page, debug=False, ssl_check=True):
        self.__headers = {
            'Content-Type': 'application/json',
            'Fineract-Platform-TenantId': tenant
        }
        self.__locale = 'en'
        self.__date_format = 'yyyy-MM-dd HH:mm:ss'
        self.__auth = HTTPBasicAuth(username, password)
        self.__timeout = timeout
        o = urlparse(base_url)
        if o.scheme != 'https':
            assert False, 'A https scheme is required'

        self.__base_url = base_url[:-1] if base_url[-1] == '/' else base_url
        self.per_page = per_page
        self._debug = debug
        self.__ssl_check = ssl_check
        self.__format_json = functools.partial(json.dumps, indent=2, sort_keys=True)
        self.__indent = functools.partial(indent, prefix='  ')

    def make_request(self, method, url, **kwargs) -> Union[Dict, bytes]:
        url = self.__base_url + url
        kwargs['auth'] = self.__auth
        kwargs['headers'] = {x: self.__headers[x] for x in self.__headers.keys()}
        if 'content_type' in kwargs:
            del kwargs['headers']['Content-Type']
            del kwargs['content_type']

        if 'accept' in kwargs:
            kwargs['headers']['accept'] = kwargs['accept']
            del kwargs['accept']

        # kwargs['verify'] = self.__ssl_check
        kwargs = self.__inject_extras(kwargs)
        kwargs['method'] = method
        kwargs['url'] = url
        is_file = False
        if 'is_file' in kwargs:
            is_file = True
            del kwargs['is_file']
        req = requests.Request(**kwargs)
        with requests.Session() as sess:
            prep_req = sess.prepare_request(req)
            if self._debug:
                print(self.format_request(prep_req))

            try:
                # res = requests.request(method, url, **kwargs)
                res = sess.send(prep_req, verify=self.__ssl_check)
            except Exception as e:
                raise self.__create_exception(500, str(e))

        if res.status_code == 204:
            e = HTTPError('No content for the requested ur', response=res)
            raise self.__create_exception(500, str(e))

        if self._debug:
            print(self.format_response(res))

        if not res.ok:
            err_data = res.json()
            message = self.__create_err_message(err_data)
            raise self.__create_exception(res.status_code, message)
        else:
            return res.json() if not is_file else res.content

    def format_request(self, req) -> str:
        headers = '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items())
        content_type = req.headers.get('Content-Type', '')
        if 'application/json' in content_type and req.body is not None:
            try:
                temp = req.body.decode('utf-8') if isinstance(req.body, bytes) else req.body
                body = self.__format_json(json.loads(temp))
            except json.JSONDecodeError:
                body = req.body
        else:
            if 'multipart/form-data' in content_type:
                body = ''
            else:
                body = req.body or ''
        s = textwrap.dedent("""
            REQUEST
            =======
            endpoint: {method} {url}
            headers:
            {headers}
            body:
            {body}
            =======
            """).strip()
        s = s.format(
            method=req.method,
            url=req.url,
            headers=self.__indent(headers),
            body=self.__indent(body),
        )
        return s

    def format_response(self, resp) -> str:
        headers = '\n'.join('{}: {}'.format(k, v) for k, v in resp.headers.items())
        content_type = resp.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            try:
                body = self.__format_json(resp.json())
            except json.JSONDecodeError:
                body = resp.text
        else:
            if 'Content-Disposition' not in resp.headers:
                body = resp.text
            else:
                body = ''
        s = textwrap.dedent("""
            RESPONSE
            ========
            status_code: {status_code}
            headers:
            {headers}
            body:
            {body}
            ========
            """).strip()

        s = s.format(
            status_code=resp.status_code,
            headers=self.__indent(headers),
            body=self.__indent(body),
        )
        return s

    def __inject_extras(self, kwargs) -> dict:
        payload = None
        if 'data' in kwargs:
            payload = kwargs['data']

        if 'json' in kwargs:
            payload = kwargs['json']

        if payload:
            extras = {}
            for key in payload.keys():
                if isinstance(payload[key], datetime.datetime):
                    extras['locale'] = self.__locale
                    extras['dateFormat'] = self.__date_format
                    extras[key] = self.__date_string(payload[key])

            payload.update(extras)

        if 'data' in kwargs:
            kwargs['data'] = payload

        if 'json' in kwargs:
            kwargs['json'] = payload

        return kwargs

    @staticmethod
    def __date_string(date) -> str:
        return date.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __create_err_message(data) -> str:
        if 'defaultUserMessage' in data:
            message = data['defaultUserMessage']
            if 'errors' in message:
                message += ' {}'.format([item['defaultUserMessage'] for item in data['errors']])
        elif 'message' in data:
            message = '{}: {}'.format(data['error'], data['message'])
        else:
            message = str(data)

        return message

    @staticmethod
    def __create_exception(status, output) -> Union[FineractException]:
        mappings = {
            '400': BadArgsException,
            '401': BadCredentialsException,
            '403': BadCredentialsException,
            '404': ResourceNotFoundException
        }
        cls = mappings.get(str(status), FineractException)

        return cls(status, output)

    @property
    def base_url(self):
        return self.__base_url
