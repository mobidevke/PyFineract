from fineract.objects.fineract_object import FineractObject


class Role(FineractObject):
    """
    This class represents a Role
    """

    def __repr__(self):
        return self.get__repr__({'name': self.name})

    def _init_attributes(self):
        self.id = None
        self.name = None
        self.description = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.description = attributes.get('description', None)
