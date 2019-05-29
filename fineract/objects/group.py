from fineract.objects.fineract_object import DataFineractObject
from fineract.objects.types import Type


class Group(DataFineractObject):
    """
    This class represents a Group.
    """
    def __repr__(self):
        return self.get__repr__({'group_id': self.id})

    def _init_attributes(self):
        self.id = None
        self.account_no = None
        self.external_id = None
        self.name = None
        self.status = None
        self.active = None
        self.activation_date = None
        self.office_id = None
        self.office_name = None
        self.hierarchy = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.account_no = attributes.get('accountNo', None)
        self.external_id = attributes.get('externalId', None)
        self.name = attributes.get('name', None)
        self.status = self._make_fineract_object(GroupStatus, attributes.get('status', None))
        self.active = attributes.get('active', None)
        self.activation_date = self._make_date_object(attributes.get('activationDate', None))
        self.office_id = attributes.get('officeId', None)
        self.office_name = attributes.get('officeName', None)
        self.hierarchy = attributes.get('hierarchy', None)


class GroupStatus(Type):
    """
    This class represents a Group status.
    """
    pass
