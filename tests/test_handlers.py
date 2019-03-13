import pytest
from requests import Response

from fineract import BadArgsException, ResourceNotFoundException, BadCredentialsException, FineractException
from fineract.handlers import RequestHandler


class ExampleResponse(Response):
    def __init__(self, code):
        super(ExampleResponse, self).__init__()
        self.status_code = code

    def json(self, **kwargs):
        return {}


ERROR_MSG = {
    "developerMessage": "The request was invalid. This typically will happen due to validation errors which are provided.",
    "developerDocLink": "https://github.com/openMF/mifosx/wiki/HTTP-API-Error-codes",
    "httpStatusCode": "400",
    "defaultUserMessage": "Validation errors exist.",
    "userMessageGlobalisationCode": "validation.msg.validation.errors.exist",
    "errors": [
        {
            "developerMessage": "The parameter name cannot be blank.",
            "defaultUserMessage": "The parameter name cannot be blank.",
            "userMessageGlobalisationCode": "validation.msg.office.name.cannot.be.blank",
            "parameterName": "name",
            "value": None,
            "args": []
        },
        {
            "developerMessage": "The parameter openingDate cannot be blank.",
            "defaultUserMessage": "The parameter openingDate cannot be blank.",
            "userMessageGlobalisationCode": "validation.msg.office.openingDate.cannot.be.blank",
            "parameterName": "openingDate", "value": None, "args": []
        },
        {
            "developerMessage": "The parameter parentId cannot be blank.",
            "defaultUserMessage": "The parameter parentId cannot be blank.",
            "userMessageGlobalisationCode":
                "validation.msg.office.parentId.cannot.be.blank", "parameterName":
            "parentId", "value": None, "args": []
        }
    ]
}


def test_request_handler__error_raised_on_none_https():
    with pytest.raises(AssertionError):
        RequestHandler('a', 'b', 'http://localhost', 'default', 10, 30)


def test_request_handler__base_url_ending_slash_removed():
    request_handler = RequestHandler('a', 'b', 'https://localhost/', 'default', 10, 30)
    assert request_handler.base_url == 'https://localhost'


def test_request_handler__make_request_BadArgsException_raised(mocker):
    with pytest.raises(BadArgsException):
        request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)
        mocker.patch('requests.request', return_value=ExampleResponse(400))
        mocker.patch.object(request_handler, '_RequestHandler__create_err_message', return_value='Failed')
        request_handler.make_request('get', '')


def test_request_handler__make_request_ResourceNotFoundException_raised(mocker):
    with pytest.raises(ResourceNotFoundException):
        request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)
        mocker.patch('requests.request', return_value=ExampleResponse(404))
        mocker.patch.object(request_handler, '_RequestHandler__create_err_message', return_value='Failed')
        request_handler.make_request('get', '')


def test_request_handler__make_request_BadCredentialsException_raised_403(mocker):
    with pytest.raises(BadCredentialsException):
        request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)
        mocker.patch('requests.request', return_value=ExampleResponse(403))
        mocker.patch.object(request_handler, '_RequestHandler__create_err_message', return_value='Failed')
        request_handler.make_request('get', '')


def test_request_handler__make_request_BadCredentialsException_raised_401(mocker):
    with pytest.raises(BadCredentialsException):
        request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)
        mocker.patch('requests.request', return_value=ExampleResponse(401))
        mocker.patch.object(request_handler, '_RequestHandler__create_err_message', return_value='Failed')
        request_handler.make_request('get', '')


def test_request_handler__make_request_FineractException_raised(mocker):
    with pytest.raises(FineractException):
        request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)
        mocker.patch('requests.request', return_value=ExampleResponse(500))
        mocker.patch.object(request_handler, '_RequestHandler__create_err_message', return_value='Failed')
        request_handler.make_request('get', '')


def test_request_handler__successful_response(mocker):
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)
    mocker.patch('requests.request', return_value=ExampleResponse(200))
    assert request_handler.make_request('get', '') == {}


def test_request_handler__create_err_message():
    request_handler = RequestHandler('a', 'b', 'https://localhost', 'default', 10, 30)
    msg = request_handler._RequestHandler__create_err_message(ERROR_MSG)
    assert msg == "Validation errors exist. ['The parameter name cannot be blank.', " \
                  "'The parameter openingDate cannot be blank.', 'The parameter parentId cannot be blank.']"
