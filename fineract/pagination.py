class PaginatedListBase:

    def __init__(self):
        self.__elements = list()

    def __getitem__(self, index):
        assert isinstance(index, (int, slice))
        if isinstance(index, int):
            self.__fetch_to_index(index)
            return self.__elements[index]
        else:
            return Slice(self, index)

    def __iter__(self):
        for element in self.__elements:
            yield element

        while self._could_grow():
            new_elements = self._grow()
            for element in new_elements:
                yield element

    def _is_bigger_than(self, index):
        return len(self.__elements) > index or self._could_grow()

    def __fetch_to_index(self, index):
        while len(self.__elements) <= index and self._could_grow():
            self._grow()

    def _could_grow(self):
        pass

    def _fetch_next_page(self):
        pass

    def _grow(self):
        new_elements = self._fetch_next_page()
        self.__elements += new_elements
        return new_elements


class Slice:

    def __init__(self, the_list, the_slice):
        self.__list = the_list
        self.__start = the_slice.start or 0
        self.__stop = the_slice.stop
        self.__step = the_slice.step or 1

    def __iter__(self):
        index = self.__start
        while not self.__finished(index):
            if self.__list._is_bigger_than(index):
                yield self.__list[index]
                index += self.__step
            else:
                return

    def __finished(self, index):
        return self.__stop is not None and index >= self.__stop


class PaginatedListLegacy(PaginatedListBase):
    """This class represents a paginated list of items fetched from a Fineract API


    :param klass: Child class of a :class:`fineract.objects.fineract_object.FineractObject`
    :param request_handler: :class:`fineract.handlers.RequestHandler`
    :param url: Endpoint to be called
    :param params: dict Extra payload to pass during the call
    :param list_item: Response field holding the items
    """
    def __init__(self, klass, request_handler, url, params, list_item='pageItems'):
        PaginatedListBase.__init__(self)
        self.__request_handler = request_handler
        self.__klass = klass
        self.__url = url
        self.__params = params or {'offset': 0}
        self.__next_offset = 0
        self.__last_offset = None
        self.__list_item = list_item
        self._is_paginated = False
        if self.__request_handler.per_page != 30:
            self.__params['limit'] = self.__request_handler.per_page
        self.__total_count = None

    @property
    def total_count(self):
        """Returns total count of items"""
        if not self.__total_count:
            data = self.__request_handler.make_request(
                'GET',
                self.__url,
                params={'limit': 1}  # not required, however it helps reduce query load on server
            )
            if isinstance(data, list):
                self.__total_count = len(data)
            else:
                data = data if data else {}
                if 'totalFilteredRecords' in data:
                    self.__total_count = data.get('totalFilteredRecords')
                else:
                    self.__total_count = 0

        return self.__total_count

    def _could_grow(self):
        return self.__next_offset is not None

    def _fetch_next_page(self):
        params = self.__params.copy()
        params['offset'] = self.__next_offset
        data = self.__request_handler.make_request(
            'GET',
            self.__url,
            params=params
        )
        data = data if data else {}

        self.__next_offset = None

        if isinstance(data, dict):
            if self.__list_item in data:
                self.__total_count = data.get('totalFilteredRecords')
                data = data[self.__list_item]
            else:
                data = []

        content = [
            self.__klass(self.__request_handler, element, False)
            for element in data if element is not None
        ]

        return content

    def get_page(self, page):
        """Get items from a specific page

        :param page: int Page number
        :return: list of :class:`fineract.objects.fineract_object.FineractObject`
        """
        params = dict(self.__params)
        if page != 0:
            params['offset'] = page - 1

        if self.__request_handler.per_page != 30:
            params['limit'] = self.__request_handler.per_page

        data = self.__request_handler.make_request(
            'GET',
            self.__url,
            params=params
        )

        if self.__list_item in data:
            self.__total_count = data.get('totalFilteredRecords')
            data = data[self.__list_item]

        return [
            self.__klass(self.__request_handler, element, False)
            for element in data
        ]


class PaginatedList:
    """This class represents a paginated list of items fetched from a Fineract API


    :param klass: Child class of a :class:`fineract.objects.fineract_object.FineractObject`
    :param request_handler: :class:`fineract.handlers.RequestHandler`
    :param url: Endpoint to be called
    :param params: dict Extra payload to pass during the call
    :param list_item: Response field holding the items
    """
    def __init__(self, klass, request_handler, url, params, list_item='pageItems'):
        self._request_handler = request_handler
        self._klass = klass
        self._url = url
        self._params = params or {'offset': 0}
        self._params = params or {}
        if 'offset' not in self._params:
            self._params['offset'] = 0
        self._params['limit'] = self._request_handler.per_page
        self._list_item = list_item
        self._total_count = None
        self._no_pagination = None
        self._elements = list()
        self._load_data()

    def _load_data(self):
        data = self._request_handler.make_request(
            'GET',
            self._url,
            params=self._params
        )
        data = data if data else {}
        if isinstance(data, dict):
            if self._list_item in data:
                self.__total_count = data.get('totalFilteredRecords')
                data = data[self._list_item]
            else:
                data = []
        else:
            self._no_pagination = True

        self._elements = [
            self._klass(self._request_handler, element, False)
            for element in data if element is not None
        ]

    @property
    def total_count(self):
        """Returns total count of items"""
        if self._total_count is None:
            self._total_count = len(self._elements)

        return self._total_count

    def get_next(self):
        """Load next page of items"""
        self._params['offset'] = (self._params['offset'] + 1) * self._params['limit']
        self._load_data()

    def has_next(self):
        """Check if there is another page

        :rtype: bool
        """
        if self._no_pagination:
            return False

        return any(self._elements)

    def __iter__(self):
        for element in self._elements:
            yield element

    def __getitem__(self, item):
        return self._elements[item]
