import math


class PaginatedList:
    """This class represents a paginated list of items fetched from a Fineract API


    :param klass: Child class of a :class:`fineract.objects.fineract_object.FineractObject`
    :param request_handler: :class:`fineract.handlers.RequestHandler`
    :param url: Endpoint to be called
    :param params: dict Extra payload to pass during the call
    :param list_item: Response field holding the items
    :param page: int Page to return
    """
    def __init__(self, klass, request_handler, url, params, list_item='pageItems', page=1):
        self._request_handler = request_handler
        self._klass = klass
        self._url = url
        self._params = params or {}
        self._params['limit'] = self._request_handler.per_page
        self._params['offset'] = (page - 1) * self._params['limit']
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

    @property
    def total_pages(self):
        """Return total pages"""
        total = self.total_count
        if self._no_pagination and total:
            return 1

        return math.ceil(total / self._params['limit'])

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
