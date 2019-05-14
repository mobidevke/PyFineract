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

    def activate(self, date=None):
        """Activates a client

        :param date: Date of client activation
        :return: bool
        """
        if date is None:
            date = self._get_current_date()

        _id = getattr(self, 'id', None)
        res = self._request_handler.make_request(
            'POST',
            '/clients/{}?command=activate'.format(_id),
            {'activationDate': date}
        )
        return res.get('clientId', None) == _id

    def close(self, closure_reason_id, date=None):
        """Close a client

        :param closure_reason_id: Closure reason id
        :param date: Date of client close
        :return: bool
        """
        if date is None:
            date = self._get_current_date()

        _id = getattr(self, 'id', None)
        res = self._request_handler.make_request(
            'POST',
            '/clients/{}?command=close'.format(_id),
            {
                'closureDate': date,
                'closureReasonId': closure_reason_id
            }
        )
        return res.get('clientId', None) == _id

    def reject(self, rejection_reason_id, date=None):
        """Reject a client

        :param rejection_reason_id: Rejection reason id
        :param date: Date of client rejection
        :return: bool
        """
        if date is None:
            date = self._get_current_date()

        _id = getattr(self, 'id', None)
        res = self._request_handler.make_request(
            'POST',
            '/clients/{}?command=reject'.format(_id),
            {
                'rejectionDate': date,
                'rejectionReasonId': rejection_reason_id
            }
        )
        return res.get('clientId', None) == _id

    def withdraw(self, withdrawal_reason_id, date=None):
        """Withdraw a client

        :param withdrawal_reason_id: Withdrawal reason id
        :param date: Date of client rejection
        :return: bool
        """
        if date is None:
            date = self._get_current_date()

        _id = getattr(self, 'id', None)
        res = self._request_handler.make_request(
            'POST',
            '/clients/{}?command=withdraw'.format(_id),
            {
                'withdrawalDate': date,
                'withdrawalReasonId': withdrawal_reason_id
            }
        )
        return res.get('clientId', None) == _id

    def reactivate(self, date=None):
        """Reactivate a client

        :param date: Date of client reactivation
        :return: bool
        """
        if date is None:
            date = self._get_current_date()

        _id = getattr(self, 'id', None)
        res = self._request_handler.make_request(
            'POST',
            '/clients/{}?command=reactivate'.format(_id),
            {'reactivationDate': date}
        )
        return res.get('clientId', None) == _id

    def undo_reject(self, date=None):
        """Undo client rejection

        :param date: Date of client rejection undoing
        :return: bool
        """
        if date is None:
            date = self._get_current_date()

        _id = getattr(self, 'id', None)
        res = self._request_handler.make_request(
            'POST',
            '/clients/{}?command=UndoRejection'.format(_id),
            {'reopenedDate': date}
        )
        return res.get('clientId', None) == _id

    def undo_withdrawal(self, date=None):
        """Undo client withdrawal

        :param date: Date of client withdrawal undoing
        :return: bool
        """
        if date is None:
            date = self._get_current_date()

        _id = getattr(self, 'id', None)
        res = self._request_handler.make_request(
            'POST',
            '/clients/{}?command=UndoWithdrawal'.format(_id),
            {'reopenedDate': date}
        )
        return res.get('clientId', None) == _id

    def get_loans(self):
        """Get the loans of a client

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

    def get_outstanding_loans(self):
        """Get the outstanding loans of a client

        """
        return [loan for loan in self.get_loans() if loan.status.active]

    def get_loans_in_arrears(self):
        """Get loans in arrears
        """
        return [loan for loan in self.get_loans() if loan.in_arrears or
                (loan.status.closed and loan.timeline.closed_on_date > loan.timeline.expected_maturity_date)]

    @classmethod
    def get_client_by_phone_no(cls, request_handler, phone_no):
        params = {
            'sqlSearch': 'c.mobile_no={}'.format(phone_no)
        }
        data = request_handler.make_request(
            'GET',
            '/clients',
            params=params
        )
        if data and data['pageItems']:
            return cls(request_handler, data['pageItems'][0], False)

        return None


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
