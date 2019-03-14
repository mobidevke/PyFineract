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


class PaginatedList(PaginatedListBase):

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
