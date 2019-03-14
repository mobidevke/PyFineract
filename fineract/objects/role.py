from fineract.objects.fineract_object import FineractObject


class Role(FineractObject):
    """
    This class represents a Role
    """

    def __repr__(self):
        return self.get__repr__({'name': self._name})

    @property
    def id(self):
        """
        :type: int
        """
        return self.id

    @property
    def name(self):
        """
        :type: str
        """
        return self._name

    @property
    def description(self):
        """
        :type: str
        """
        return self._description

    def _init_attributes(self):
        self._id = None
        self._name = None
        self._description = None

    def _use_attributes(self, attributes):
        self._id = attributes.get('id', None)
        self._name = attributes.get('name', None)
        self._description = attributes.get('description', None)
