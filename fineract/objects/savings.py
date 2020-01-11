from datetime import datetime

from fineract.objects.currency import Currency
from fineract.objects.fineract_object import FineractObject
from fineract.objects.types import Type


class Savings(FineractObject):
    """
    This class represents Savings.
    """

    def _init_attributes(self):
        self.id = None
        self.account_no = None
        self.deposit_type = None
        self.client_id = None
        self.client_name = None
        self.savings_product_id = None
        self.savings_product_name = None
        self.field_officer_id = None
        self.status = None
        self.sub_status = None
        self.timeline = None
        self.currency = None
        self.nominal_annual_interest_rate = None
        self.interest_compounding_period_type = None
        self.interest_posting_period_type = None
        self.interest_calculation_type = None
        self.interest_calculation_days_in_year_type = None
        self.min_required_opening_balance = None
        self.lockin_period_frequency = None
        self.lockin_period_frequency_type = None
        self.withdrawal_fee_for_transfers = None
        self.allow_overdraft = None
        self.enforce_min_required_balance = None
        self.with_hold_tax = None
        self.last_active_transaction_date = None
        self.is_dormancy_tracking_active = None
        self.savings_amount_on_hold = None
        self.summary = None
        self.transactions = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.account_no = attributes.get('accountNo', None)
        self.deposit_type = self._make_fineract_object(Type, attributes.get('depositType', None))
        self.client_id = attributes.get('clientId', None)
        self.client_name = attributes.get('clientName', None)
        self.savings_product_id = attributes.get('savingsProductId', None)
        self.savings_product_name = attributes.get('savingsProductName', None)
        self.field_officer_id = attributes.get('fieldOfficerId', None)
        self.status = self._make_fineract_object(SavingsStatus, attributes.get('status', None))
        self.sub_status = self._make_fineract_object(SavingsSubStatus, attributes.get('subStatus', None))
        self.timeline = self._make_fineract_object(SavingsTimeline, attributes.get('timeline', None))
        self.currency = self._make_fineract_object(Currency, attributes.get('currency', None))
        self.nominal_annual_interest_rate = attributes.get('nominalAnnualInterestRate', None)
        self.interest_compounding_period_type = self._make_fineract_object(Type, attributes.get(
            'interestCompoundingPeriodType', None))
        self.interest_posting_period_type = self._make_fineract_object(Type, attributes.get('interestPostingPeriodType',
                                                                                            None))
        self.interest_calculation_type = self._make_fineract_object(Type,
                                                                    attributes.get('interestCalculationType', None))
        self.interest_calculation_days_in_year_type = self._make_fineract_object(Type, attributes.get(
            'interestCalculationDaysInYearType', None))
        self.min_required_opening_balance = attributes.get('minRequiredOpeningBalance', None)
        self.lockin_period_frequency = attributes.get('lockinPeriodFrequency', None)
        self.lockin_period_frequency_type = self._make_fineract_object(Type, attributes.get('lockinPeriodFrequencyType',
                                                                                            None))
        self.withdrawal_fee_for_transfers = attributes.get('withdrawalFeeForTransfers', None)
        self.allow_overdraft = attributes.get('allowOverdraft', None)
        self.enforce_min_required_balance = attributes.get('enforceMinRequiredBalance', None)
        self.with_hold_tax = attributes.get('withHoldTax', None)
        self.last_active_transaction_date = self._make_date_object(attributes.get('lastActiveTransactionDate', None))
        self.is_dormancy_tracking_active = attributes.get('isDormancyTrackingActive', None)
        self.savings_amount_on_hold = attributes.get('savingsAmountOnHold', None)
        self.summary = self._make_fineract_object(SavingsSummary, attributes.get('summary', None))
        self.transactions = self._make_date_object(attributes.get('transactions', None))

    @classmethod
    def apply(cls, request_handler, client_id, product_id, submitted_on_date=datetime.now()) -> 'Savings':
        """

        :param request_handler:
        :param client_id:
        :param product_id:
        :param submitted_on_date:
        :return: :class:`fineract.objects.savings.Savings`
        """
        payload = {
            'clientId': client_id,
            'productId': product_id,
            'submittedOnDate': submitted_on_date
        }
        res = request_handler.make_request(
            'POST',
            '/savingsaccounts',
            json=payload
        )

        savings_id = res['savingsId']
        return cls(request_handler,
                   request_handler.make_request(
                       'GET',
                       '/savingsaccounts/{}'.format(savings_id)
                   ), False)

    def approve(self, approved_on_date=datetime.now()) -> bool:
        """Approve a savings application

        :param approved_on_date:
        :return: bool
        """
        payload = {
            'approvedOnDate': approved_on_date
        }

        res = self.request_handler.make_request(
            'POST',
            '/savingsaccounts/{}?command=approve'.format(self.id),
            json=payload
        )
        return res['savingsId'] == self.id

    def undo_approve(self) -> bool:
        """Undo savings application approval

        :return: bool
        """
        res = self.request_handler.make_request(
            'POST',
            '/savingsaccounts/{}?command=undoApproval'.format(self.id),
            json={}
        )
        return res['savingsId'] == self.id

    def activate(self, activated_on_date=datetime.now()) -> bool:
        """Activate a savings account

        :param activated_on_date:
        :return: bool
        """
        payload = {
            'activatedOnDate': activated_on_date
        }

        res = self.request_handler.make_request(
            'POST',
            '/savingsaccounts/{}?command=activate'.format(self.id),
            json=payload
        )
        return res['savingsId'] == self.id

    # def close(self, closed_on_date=datetime.now(), withdraw_balance=False):
    #     """Close a savings account
    #
    #     :param closed_on_date:
    #     :return: bool
    #     """
    #     payload = {
    #         'closedOnDate': closed_on_date,
    #         'withdrawBalance': withdraw_balance
    #     }
    #
    #     res = self.request_handler.make_request(
    #         'POST',
    #         '/savingsaccounts/{}?command=close'.format(self.id),
    #         json=payload
    #     )
    #     return res['savingsId'] == self.id


class SavingsStatus(FineractObject):

    def _init_attributes(self):
        self.id = None
        self.code = None
        self.value = None
        self.submitted_and_pending_approval = None
        self.approved = None
        self.rejected = None
        self.withdrawn_by_applicant = None
        self.active = None
        self.closed = None
        self.premature_closed = None
        self.transfer_in_progress = None
        self.transfer_on_hold = None
        self.matured = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.code = attributes.get('code', None)
        self.value = attributes.get('value', None)
        self.submitted_and_pending_approval = attributes.get('submittedAndPendingApproval', None)
        self.approved = attributes.get('approved', None)
        self.rejected = attributes.get('rejected', None)
        self.withdrawn_by_applicant = attributes.get('withdrawnByApplicant', None)
        self.active = attributes.get('active', None)
        self.closed = attributes.get('closed', None)
        self.premature_closed = attributes.get('prematureClosed', None)
        self.transfer_in_progress = attributes.get('transferInProgress', None)
        self.transfer_on_hold = attributes.get('transferOnHold', None)
        self.matured = attributes.get('matured', None)


class SavingsSubStatus(FineractObject):

    def _init_attributes(self):
        self.id = None
        self.code = None
        self.value = None
        self.none = None
        self.inactive = None
        self.dormant = None
        self.escheat = None
        self.block = None
        self.block_credit = None
        self.block_debit = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.code = attributes.get('code', None)
        self.value = attributes.get('value', None)
        self.none = attributes.get('none', None)
        self.inactive = attributes.get('inactive', None)
        self.dormant = attributes.get('dormant', None)
        self.escheat = attributes.get('escheat', None)
        self.block = attributes.get('block', None)
        self.block_credit = attributes.get('blockCredit', None)
        self.block_debit = attributes.get('blockDebit', None)


class SavingsTimeline(FineractObject):

    def _init_attributes(self):
        self.submitted_on_date = None
        self.submitted_by_username = None
        self.submitted_by_firstname = None
        self.submitted_by_lastname = None
        self.approved_on_date = None
        self.approved_by_username = None
        self.approved_by_firstname = None
        self.approved_by_lastname = None
        self.activated_on_date = None
        self.activated_by_username = None
        self.activated_by_firstname = None
        self.activated_by_lastname = None

    def _use_attributes(self, attributes):
        self.submitted_on_date = self._make_date_object(attributes.get('submittedOnDate', None))
        self.submitted_by_username = attributes.get('submittedByUsername', None)
        self.submitted_by_firstname = attributes.get('submittedByFirstname', None)
        self.submitted_by_lastname = attributes.get('submittedByLastname', None)
        self.approved_on_date = self._make_date_object(attributes.get('approvedOnDate', None))
        self.approved_by_username = attributes.get('approvedByUsername', None)
        self.approved_by_firstname = attributes.get('approvedByFirstname', None)
        self.approved_by_lastname = attributes.get('approvedByLastname', None)
        self.activated_on_date = self._make_date_object(attributes.get('activatedOnDate', None))
        self.activated_by_username = attributes.get('activatedByUsername', None)
        self.activated_by_firstname = attributes.get('activatedByFirstname', None)
        self.activated_by_lastname = attributes.get('activatedByLastname', None)


class SavingsSummary(FineractObject):

    def _init_attributes(self):
        self.currency = None
        self.total_deposits = None
        self.total_withdrawals = None
        self.total_interest_earned = None
        self.total_interest_posted = None
        self.account_balance = None
        self.total_overdraft_interest_derived = None
        self.interest_not_posted = None
        self.last_interest_calculation_date = None
        self.available_balance = None

    def _use_attributes(self, attributes):
        self.currency = self._make_fineract_object(Currency, attributes.get('currency', None))
        self.total_deposits = attributes.get('totalDeposits', None)
        self.total_withdrawals = attributes.get('totalWithdrawals', None)
        self.total_interest_earned = attributes.get('totalInterestEarned', None)
        self.total_interest_posted = attributes.get('totalInterestPosted', None)
        self.account_balance = attributes.get('accountBalance', None)
        self.total_overdraft_interest_derived = attributes.get('totalOverdraftInterestDerived', None)
        self.interest_not_posted = attributes.get('interestNotPosted', None)
        self.last_interest_calculation_date = self._make_date_object(
            attributes.get('lastInterestCalculationDate', None))
        self.available_balance = attributes.get('availableBalance', None)
