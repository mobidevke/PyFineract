from fineract.objects.fineract_object import FineractObject, DataFineractObject
from fineract.objects.loan import Loan
from fineract.objects.types import Type
from fineract.pagination import PaginatedList


class Client(DataFineractObject):
    """
    This class represents a Client.
    """

    def __repr__(self):
        return self.get__repr__({'client_id': self.id})

    def _init_attributes(self):
        self.id = None
        self.account_no = None
        self.external_id = None
        self.status = None
        self.active = None
        self.activation_date = None
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.full_name = None
        self.mobile_no = None
        self.date_of_birth = None
        self.office_id = None
        self.office_name = None
        self.savings_product_id = None
        self.type = None
        self.timeline = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.account_no = attributes.get('accountNo', None)
        self.external_id = attributes.get('externalId', None)
        self.status = self._make_fineract_object(ClientStatus, attributes.get('status', None))
        self.active = attributes.get('active', None)
        self.activation_date = self._make_date_object(attributes.get('activationDate', None))
        self.first_name = attributes.get('firstname', None)
        self.last_name = attributes.get('lastname', None)
        self.middle_name = attributes.get('middlename', None)
        self.full_name = attributes.get('displayName', None)
        self.mobile_no = attributes.get('mobileNo', None)
        self.date_of_birth = self._make_date_object(attributes.get('dateOfBirth', None))
        self.office_id = attributes.get('officeId', None)
        self.office_name = attributes.get('officeName', None)
        self.savings_product_id = attributes.get('savingsAccountId', None)
        self.type = self._make_fineract_object(ClientType, attributes.get('clientType', None))
        self.timeline = self._make_fineract_object(ClientTimeline, attributes.get('timeline', None))

    def get_loans(self):
        """
        Get the loans of a client
        """
        _id = getattr(self, 'id', None)
        if _id:
            return PaginatedList(
                Loan,
                self._request_handler,
                '/loans',
                dict(sqlSearch='l.client_id={}'.format(self.id))
            )
        raise AttributeError('id not set')


class ClientStatus(Type):
    """
    This class represents a Client status.
    """
    pass


class ClientType(FineractObject):

    def _init_attributes(self):
        self.id = None
        self.name = None
        self.active = None
        self.mandatory = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.active = attributes.get('active', None)
        self.mandatory = attributes.get('mandatory', None)


class ClientTimeline(FineractObject):
    """
    This class represents the timeline of a Client
    """

    def _init_attributes(self):
        self.submitted_on_date = None
        self.submitted_by = None
        self.activated_on = None
        self.activated_by = None

    def _use_attributes(self, attributes):
        self.submitted_on_date = self._make_date_object(attributes.get('submittedOnDate', None))
        self.submitted_by = attributes.get('submittedByUsername', None)
        self.activated_on_date = self._make_date_object(attributes.get('activatedOnDate', None))
        self.activated_by = attributes.get('activatedByUsername', None)
