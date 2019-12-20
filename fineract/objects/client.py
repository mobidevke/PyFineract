import datetime

from fineract.objects.document import Document
from fineract.objects.fineract_object import FineractObject, DataFineractObject
from fineract.objects.group import Group
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
        self.groups = None

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
        self.groups = self._make_fineract_objects_list(Group, attributes.get('groups', None))

    def update(self, data):
        """Update the core fields of a client

        :param data: dict
        """
        _id = getattr(self, 'id', None)
        res = self._request_handler.make_request(
            'PUT',
            '/clients/{}'.format(_id),
            json=data
        )
        assert res.get('clientId', None) == _id

    def delete(self):
        """Deletes a client (Must be in pending state)"""
        res = self._request_handler.make_request(
            'DELETE',
            '/clients/{}'.format(self.id),
        )
        assert res.get('clientId', None) == self.id

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

    def add_document(self, name, description, file, filename):
        """Add  a document to client

        :param name:
        :param description:
        :param file:
        :param filename:
        :rtype: :class:`fineract.objects.document.Document`
        """
        return Document.create(self._request_handler, Document.CLIENTS, self.id, name, description, file, filename)

    def documents(self):
        """Get all documents for a client

        :rtype: list of :class:`fineract.objects.document.Document`
        """
        return Document.get_all(self._request_handler, Document.CLIENTS, self.id)

    def document(self, document_id):
        """Get a document that matches ``document_id``

        :param document_id:
        :rtype: :class:`fineract.objects.document.Document`
        """
        return Document.get(self._request_handler, Document.CLIENTS, self.id, document_id)

    def get_loans(self):
        """Get the loans of a client

        :rtype: list of :class:`fineract.objects.loan.Loan`
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

        :rtype: list of :class:`fineract.objects.loan.Loan`
        """
        return [loan for loan in self.get_loans() if loan.status.active]

    def get_loans_in_arrears(self, active=True, all_loans=False):
        """Get loans in arrears

        :param active: boolean flag to choose between closed/open loans
        :param all_loans: flag to choose between returning all loans in arrears or specific loans based on active
               parameter
        :rtype: list of :class:`fineract.objects.loan.Loan`
        """
        now = datetime.datetime.now().date()
        if all_loans:
            return [loan for loan in self.get_loans() if
                    (loan.in_arrears or (now > loan.timeline.expected_maturity_date.date())) or
                    (loan.status.closed and loan.timeline.closed_on_date > loan.timeline.expected_maturity_date)]

        if active:
            return [loan for loan in self.get_loans() if
                    (loan.in_arrears or (now > loan.timeline.expected_maturity_date.date())) and loan.status.active]
        else:
            return [loan for loan in self.get_loans() if loan.status.closed and loan.timeline.closed_on_date >
                    loan.timeline.expected_maturity_date]

    def set_image(self, file, filename, content_type='image/png'):
        """Set the image for a client. Pass `None` to delete an image.

        :param file:
        """
        if file is None:
            data = self.request_handler.make_request(
                'DELETE',
                '/clients/{}/images'.format(self.id),
            )
            return data['resourceId'] == self.id
        else:
            file_descr = (filename, file, content_type)
            params = {
                'file': file_descr
            }
            data = self.request_handler.make_request(
                'POST',
                '/clients/{}/images'.format(self.id),
                files=params,
                content_type='multipart/form-data'
            )
            return data['resourceId'] == self.id

    def download_image(self):
        """Download a document

        :return: file content
        """
        return self._request_handler.make_request(
            'GET',
            '/clients/{}/images'.format(self.id),
            accept='application/octet-stream',
            is_file=True
        )

    @classmethod
    def get_client_by_phone_no(cls, request_handler, phone_no):
        """Get a client by phone no

        :param request_handler:
        :param phone_no:
        :rtype: :class:`fineract.objects.client.Client`
        """
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

    @classmethod
    def create(cls, request_handler, firstname, lastname, office_id, active=True, activation_date=None, mobile_no=None,
               external_id=None, group_id=None, staff_id=None, savings_product_id=None, gender_id=None,
               client_type_id=None, client_classification_id=None, account_no=None, middlename=None,
               submittedon_date=None):
        """Create a client and return a Client object

        :param account_no:
        :param client_classification_id:
        :param external_id:
        :param group_id:
        :param staff_id:
        :param savings_product_id:
        :param gender_id:
        :param client_type_id:
        :param mobile_no:
        :param request_handler:
        :param firstname:
        :param lastname:
        :param middlename:
        :param office_id:
        :param active:
        :param activation_date:
        :rtype: :class:`fineract.objects.client.Client`
        """
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'officeId': office_id,
            'active': active,
            'submittedOnDate': submittedon_date or cls._get_current_date()
        }
        if middlename:
            data['middlename'] = middlename

        if active:
            data['activationDate'] = activation_date or cls._get_current_date()

        if group_id:
            data['groupId'] = group_id

        if external_id:
            data['externalId'] = external_id

        if account_no:
            data['accountNo'] = account_no

        if staff_id:
            data['staffId'] = staff_id

        if mobile_no:
            data['mobileNo'] = mobile_no

        if savings_product_id:
            data['savingsProductId'] = savings_product_id

        if gender_id:
            data['genderId'] = gender_id

        if client_type_id:
            data['clientTypeId'] = client_type_id

        if client_classification_id:
            data['clientClassifcationId'] = client_classification_id

        res = request_handler.make_request(
            'POST',
            '/clients',
            json=data
        )

        client_id = res['clientId']
        return cls(request_handler,
                   request_handler.make_request(
                       'GET',
                       '/clients/{}'.format(client_id)
                   ), False)

    def is_activated(self):
        """
        Check if client has been activated
        :return: bool
        """
        return self.active == True


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
