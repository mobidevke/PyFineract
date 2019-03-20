from fineract.objects.fineract_object import FineractObject


class Staff(FineractObject):
    """
    This class represents a Staff
    """

    def _init_attributes(self):
        self.firstname = None
        self.lastname = None
        self.display_name = None
        self.office_id = None
        self.office_name = None
        self.is_loan_officer = None
        self.external_id = None
        self.is_active = None
        self.join_date = None

    def _use_attributes(self, attributes):
        self.firstname = attributes.get('firstname', None)
        self.lastname = attributes.get('lastname', None)
        self.display_name = attributes.get('displayName', None)
        self.office_id = attributes.get('officeId', None)
        self.office_name = attributes.get('officeName', None)
        self.is_loan_officer = attributes.get('isLoanOfficer', None)
        self.is_active = attributes.get('externalId', None)
        self.join_date = self._make_date_object(attributes.get('joiningDate', None))
