import datetime
import sys
from operator import itemgetter

at_least_python3 = sys.hexversion >= 0x03000000


class FineractObject(object):
    """
    Base class for all classes representing objects returned by the API
    """
    __fineract__ = True

    def __init__(self, request_handler, attributes, completed):
        self._request_handler = request_handler
        self.__completed = completed
        self.__url = None
        self._init_attributes()
        self._store_and_use_attributes(attributes)


    def _store_and_use_attributes(self, attributes):
        self._raw_data = attributes
        self._use_attributes(attributes)

        if attributes:
            self.__completed = True

    def _init_attributes(self):
        pass

    def _use_attributes(self, attributes):
        pass

    def _complete_if_not_set(self, value):
        if value is None:
            self._complete_if_needed()

    def _complete_if_needed(self):
        if not self.__completed:
            self.__complete()

    def __complete(self):
        data = self._request_handler.make_request('GET', self.__url)
        self._store_and_use_attributes(data)
        self.__completed = True

    @staticmethod
    def _make_date_object(date_list):
        return datetime.datetime(
            date_list[0],
            date_list[1],
            date_list[2]
        ) if date_list else date_list

    @staticmethod
    def _make_date_object_from_timestamp(dt):
        return datetime.datetime.fromtimestamp(dt / 1000) if dt else dt

    def _make_fineract_object(self, klass, attributes):
        return klass(self._request_handler, attributes, False) if attributes else attributes

    def _make_fineract_objects_list(self, klass, attributes):
        if isinstance(attributes, list):
            objects = []
            for attr in attributes:
                objects.append(
                    self._make_fineract_object(klass, attr)
                )
            return objects
        return attributes

    def get__repr__(self, params):
        """
        Converts the object to a nicely printable string.
        """

        def format_params(params1):
            if at_least_python3:
                items = params1.items()
            else:
                items = list(params1.items())
            for k, v in sorted(items, key=itemgetter(0), reverse=True):
                is_text = isinstance(v, str)
                if is_text and not at_least_python3:
                    v = v.encode('utf-8')
                yield '{k}="{v}"'.format(k=k, v=v) if is_text else '{k}={v}'.format(k=k, v=v)

        return '{class_name}({params})'.format(
            class_name=self.__class__.__name__,
            params=", ".join(list(format_params(params)))
        )

    @property
    def request_handler(self):
        return self._request_handler

    @property
    def raw_data(self):
        """
        :type dict
        """
        self._complete_if_needed()
        return self._raw_data

    @staticmethod
    def _get_current_date():
        return datetime.datetime.today()

    @staticmethod
    def _to_camel_case(string):
        string = string.title().replace('_', '')
        return string[0].lower() + string[1:]


    def as_dict(self):
        """Return dictionary representation of a :class:`fineract.objects.fineract_object.FineractObject`

        :rtype: dict
        """
        data = self.__dict__
        for key in list(data.keys()):
            if key[0] == '_':
                del data[key]
            elif data[key] and hasattr(data[key], '__fineract__') and data[key].__fineract__:
                data[key] = data[key].as_dict()
            elif isinstance(data[key], datetime.datetime):
                data[key] = data[key].strftime('%Y-%m-%d')

        if '_raw_data' in data:
            del data['_raw_data']

        return data


class DataFineractObject(FineractObject):
    """
    Base class for all classes representing objects which can be associated with a datatable
    """

    def get_datatable_data(self, datatable):
        _id = getattr(self, 'id', None)
        if _id:
            return self.request_handler.make_request(
                'GET',
                '/datatables/{}/{}'.format(datatable, _id)
            )

        raise AttributeError('id not set')
