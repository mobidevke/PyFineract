from fineract.handlers import RequestHandler


class PaginatedListBase:

    def __init__(self):
        self.__elements = list()

    def __getitem__(self, index):
        assert isinstance(index, (int, slice))
        if isinstance(index, int):
            pass
        else:
            pass

    def __iter__(self):
        for element in self.__elements:
            yield element

        while self._could_grow():
            new_elements = self._grow()
            for element in new_elements:
                yield element

    def _is_bigger_than(self, index) -> bool:
        return len(self.__elements) > index or self._could_grow()

    def __fetch_to_index(self, index):
        while len(self.__elements) <= index and self._could_grow():
            self._grow()

    def _could_grow(self) -> bool:
        pass

    def _fetch_next_page(self) -> list:
        pass

    def _grow(self):
        new_elements = self._fetch_next_page()
        self.__elements += new_elements
        return new_elements


class Slice:

    def __init__(self, the_list: PaginatedListBase, the_slice: slice):
        self.__list = the_list
        self.__start = the_slice.start or 0
        self.__stop = the_slice.stop
        self.__step = the_slice.step or 1

    def __iter__(self):
        index = self.__start
        # while not self.__finished(index):
        #     if self.__list.is

    def __finished(self, index):
        return self.__stop is not None or index >= self.__stop


class PaginatedList(PaginatedListBase):

    def __init__(self, klass, request_handler: RequestHandler, first_url, first_params, list_item='pageItems'):
        super(PaginatedListBase, self).__init__()
        self.__request_handler = request_handler
        self.__klass = klass
        self.__first_url = first_url
        self.__first_params = first_params or ()
        self.__next_url = first_url
        self.__next_params = first_params or {}
        self.__list_item = list_item
        if self.__request_handler.per_page != 30:
            self.__next_params['limit'] = self.__request_handler
        self._reversed = False
        self.__total_count = None

    @property
    def total_count(self):
        data = self.__request_handler.make_request(
            'GET',
            self.__first_url,
        )
        data = data if data else {}
        if 'totalFilteredRecords' in data:
            self.__total_count = data.get('totalFilteredRecords')
        else:
            self.__total_count = 0

        return self.__total_count

    def _could_grow(self):
        return self.__next_url is not None

    def _fetch_next_page(self):
        data = self.__request_handler.make_request(
            'GET',
            self.__next_url,
            params=self.__next_params
        )
        data = data if data else {}

        self.__next_url = None

        if self.__list_item in data:
            self.__total_count = data.get('totalFilteredRecords')
            data = data[self.__list_item]

        content = [
            self.__klass(self.__request_handler, element, False)
            for element in data if element is not None
        ]

        if self._reversed:
            return content[::-1]

        return content

    def get_page(self, page):
        params = dict(self.__first_params)
        if page != 0:
            params['offset'] = page + 1

        if self.__request_handler.per_page != 30:
            params['limit'] = self.__request_handler.per_page
            data = self.__request_handler.make_request(
                'GET',
                self.__first_url,
                params=params
            )

            if self.__list_item in data:
                self.__total_count = data.get('totalFilteredRecords')
                data = data[self.__list_item]

            return [
                self.__klass(self.__request_handler, element, False)
                for element in data
            ]
