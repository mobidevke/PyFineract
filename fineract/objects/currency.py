from fineract.objects.fineract_object import FineractObject


class Currency(FineractObject):
    """
    This class represents Currency.
    """

    def __repr__(self):
        return self.get__repr__({'name': self.code})

    def _init_attributes(self):
        self.code = None
        self.name = None
        self.decimal_places = None
        self.in_multiples_of = None
        self.display_symbol = None
        self.name_code = None
        self.display_label = None

    def _use_attributes(self, attributes):
        self.code = attributes.get('code', None)
        self.name = attributes.get('name', None)
        self.decimal_places = attributes.get('decimalPlaces', None)
        self.in_multiples_of = attributes.get('inMultiplesOf', None)
        self.display_symbol = attributes.get('displaySymbol', None)
        self.name_code = attributes.get('nameCode', None)
        self.display_label = attributes.get('displayLabel', None)
