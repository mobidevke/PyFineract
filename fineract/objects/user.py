from fineract.objects.fineract_object import FineractObject
from fineract.objects.role import Role


class User(FineractObject):
    """
    This class represents a User
    """

    def _init_attributes(self):
        self.id = None
        self.username = None
        self.office_id = None
        self.office_name = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password_never_expires = None
        self.staff = None
        self.selected_roles = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.username = attributes.get('username', None)
        self.office_id = attributes.get('officeId', None)
        self.office_name = attributes.get('officeName', None)
        self.first_name = attributes.get('firstname', None)
        self.last_name = attributes.get('lastname', None)
        self.email = attributes.get('email', None)
        self.password_never_expires = attributes.get('passwordNeverExpires', None)
        self.staff = attributes.get('staff', None)
        self.selected_roles = self._make_fineract_objects_list(Role, attributes.get('selectedRoles', None))
