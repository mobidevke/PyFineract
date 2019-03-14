from fineract.objects.fineract_object import FineractObject


class Currency(FineractObject):
    """
    This class represents Currency.
    """

    def __repr__(self):
        return self.get__repr__({'name': self._code})

    @property
    def code(self):
        """
        :type: str
        """
        return self._code

    @property
    def name(self):
        """
        :type: str
        """
        return self._name

    @property
    def decimal_places(self):
        """
        :type: int
        """
        return self._decimal_places

    @property
    def in_multiples_of(self):
        """
        :type: int
        """
        return self._in_multiples_of

    @property
    def display_symbol(self):
        """
        :type: str
        """
        return self._display_symbol

    @property
    def name_code(self):
        """
        :type: str
        """
        return self._name_code

    @property
    def display_label(self):
        """
        :type: str
        """
        return self._display_label

    def _init_attributes(self):
        self._code = None
        self._name = None
        self._decimal_places = None
        self._in_multiples_of = None
        self._display_symbol = None
        self._name_code = None
        self._display_label = None

    def _use_attributes(self, attributes):
        self._code = attributes.get('code', None)
        self._name = attributes.get('name', None)
        self._decimal_places = attributes.get('decimalPlaces', None)
        self._in_multiples_of = attributes.get('inMultiplesOf', None)
        self._display_symbol = attributes.get('displaySymbol', None)
        self._name_code = attributes.get('nameCode', None)
        self._display_label = attributes.get('displayLabel', None)
