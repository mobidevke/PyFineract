from fineract.objects.fineract_object import FineractObject, DataFineractObject
from fineract.objects.types import Type


class Client(DataFineractObject):
    """
    This class represents a Client.
    """

    def __repr__(self):
        return self.get__repr__({'client_id': self._id})

    @property
    def id(self):
        """
        :type: int
        """
        return self._id

    @property
    def account_no(self):
        """
        :type: str
        """
        return self._account_no

    @property
    def external_id(self):
        """
        :type: str
        """
        return self._external_id

    @property
    def status(self):
        """
        :type: :class:`fineract.objects.client.ClientStatus`
        """
        return self._status

    @property
    def active(self):
        """
        :type: bool
        """
        return self._active

    @property
    def activation_date(self):
        """
        :type: :class:`datetime.datetime`
        """
        return self._activation_date

    @property
    def first_name(self):
        """
        :type: str
        """
        return self._first_name

    @property
    def last_name(self):
        """
        :type: str
        """
        return self._last_name

    @property
    def middle_name(self):
        """
        :type: str
        """
        return self._middle_name

    @property
    def full_name(self):
        """
        :type: str
        """
        return self._full_name

    @property
    def mobile_no(self):
        """
        :type: str
        """
        return self._mobile_no

    @property
    def date_of_birth(self):
        """
        :type: :class:`datetime.datetime`
        """
        return self._date_of_birth

    @property
    def office_id(self):
        """
        :type: int
        """
        return self._office_id

    @property
    def office_name(self):
        """
        :type: str
        """
        return self._office_name

    @property
    def savings_product_id(self):
        """
        :type: int
        """
        return self._savings_product_id

    @property
    def type(self):
        """
        :type: :class:`fineract.objects.client.ClientType`
        """
        return self._type

    @property
    def timeline(self):
        """
        :type: :class:`fineract.objects.client.ClientTimeline`
        """
        return self._timeline

    def _init_attributes(self):
        self._id = None
        self._account_no = None
        self._external_id = None
        self._status = None
        self._active = None
        self._activation_date = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._full_name = None
        self._mobile_no = None
        self._date_of_birth = None
        self._office_id = None
        self._office_name = None
        self._savings_product_id = None
        self._type = None
        self._timeline = None

    def _use_attributes(self, attributes):
        self._id = attributes.get('id', None)
        self._account_no = attributes.get('accountNo', None)
        self._external_id = attributes.get('externalId', None)
        self._status = self.make_fineract_object(ClientStatus, attributes.get('status', None))
        self._active = attributes.get('active', None)
        self._activation_date = self.make_date_object(attributes.get('activationDate', None))
        self._first_name = attributes.get('firstname', None)
        self._last_name = attributes.get('lastname', None)
        self._middle_name = attributes.get('middlename', None)
        self._full_name = attributes.get('displayName', None)
        self._mobile_no = attributes.get('mobileNo', None)
        self._date_of_birth = self.make_date_object(attributes.get('dateOfBirth', None))
        self._office_id = attributes.get('officeId', None)
        self._office_name = attributes.get('officeName', None)
        self._savings_product_id = attributes.get('savingsAccountId', None)
        self._type = self.make_fineract_object(ClientType, attributes.get('clientType', None))
        self._timeline = self.make_fineract_object(ClientTimeline, attributes.get('timeline', None))

    def get_loans(self):
        """
        Get the loans of a client
        """
        pass


class ClientStatus(Type):
    """
    This class represents a Client status.
    """
    pass


class ClientType(FineractObject):

    @property
    def id(self):
        """
        :type: int
        """
        return self._id

    @property
    def name(self):
        """
        :type: str
        """
        return self._name

    @property
    def active(self):
        """
        :type: bool
        """
        return self._active

    @property
    def submitted_on(self):
        """
        :type: bool
        """
        return self._mandatory

    def _init_attributes(self):
        self._id = None
        self._name = None
        self._active = None
        self._mandatory = None

    def _use_attributes(self, attributes):
        self._id = attributes.get('id', None)
        self._name = attributes.get('name', None)
        self._active = attributes.get('active', None)
        self._mandatory = attributes.get('mandatory', None)


class ClientTimeline(FineractObject):
    """
    This class represents the timeline of a Client
    """

    @property
    def submitted_on(self):
        """
        :type: :class:`datetime.datetime`
        """
        return self._submitted_on_date

    @property
    def submitted_by(self):
        """
        :type: str
        """
        return self._submitted_by

    @property
    def activated_on(self):
        """
        :type: :class:`datetime.datetime`
        """
        return self._activated_on_date

    @property
    def activated_by(self):
        """
        :type: str
        """
        return self._activated_by

    def _init_attributes(self):
        self._submitted_on_date = None
        self._submitted_by = None
        self._activated_on = None
        self._activated_by = None

    def _use_attributes(self, attributes):
        self._submitted_on_date = self.make_date_object(attributes.get('submittedOnDate', None))
        self._submitted_by = attributes.get('submittedByUsername', None)
        self._activated_on_date = self.make_date_object(attributes.get('activatedOnDate', None))
        self._activated_by = attributes.get('activatedByUsername', None)
