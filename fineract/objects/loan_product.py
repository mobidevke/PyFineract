from fineract.objects.currency import Currency
from fineract.objects.fineract_object import FineractObject
from fineract.objects.interest import InterestRecalculationData
from fineract.objects.types import RepaymentFrequencyType, InterestFrequencyType, AmortizationType, InterestType, \
    InterestCalculationPeriodType, DaysInMonthType, DaysInYearType, AccountingRule


class LoanProduct(FineractObject):
    """
    This class represents a LoanProduct.
    """

    def __repr__(self):
        return self.get__repr__({'short_name': self._short_name})

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
    def short_name(self):
        """
        :type: str
        """
        return self._short_name

    @property
    def include_in_borrower_cycle(self):
        """
        :type: bool
        """
        return self._include_in_borrower_cycle

    @property
    def use_borrower_cycle(self):
        """
        :type: bool
        """
        return self._use_borrower_cycle

    @property
    def start_date(self):
        """
        :type: :class:`datetime.datetime`
        """
        return self._start_date

    @property
    def end_date(self):
        """
        :type: :class:`datetime.datetime`
        """
        return self._end_date

    @property
    def currency(self):
        """
        :type: :class:`fineract.objects.Currency`
        """
        return self._currency

    @property
    def principal(self):
        """
        :type: float
        """
        return self._principal

    @property
    def min_principal(self):
        """
        :type: float
        """
        return self._min_principal

    @property
    def max_principal(self):
        """
        :type: float
        """
        return self._max_principal

    @property
    def no_of_repayments(self):
        """
        :type: int
        """
        return self._no_of_repayments

    @property
    def min_no_of_repayments(self):
        """
        :type: int
        """
        return self._min_no_of_repayments

    @property
    def max_no_of_repayments(self):
        """
        :type: int
        """
        return self._max_no_of_repayments

    @property
    def repayment_every(self):
        """
        :type: int
        """
        return self._repayment_every

    @property
    def repayment_frequency_type(self):
        """
        :type: :class:`fineract.objects.type.RepaymentFrequencyType`
        """
        return self._repayment_frequency_type

    @property
    def interest_rate_per_period(self):
        """
        :type: int
        """
        return self._interest_rate_per_period

    @property
    def interest_rate_frequency_type(self):
        """
        :type: :class:`fineract.objects.type.InterestRateFrequencyType`
        """
        return self._interest_rate_frequency_type

    @property
    def annual_interest_rate(self):
        """
        :type: float
        """
        return self._annual_interest_rate

    @property
    def amortization_type(self):
        """
        :type: :class:`fineract.objects.type.AmortizationType`
        """
        return self._amortization_type

    @property
    def interest_type(self):
        """
        :type: :class:`fineract.objects.type.InterestType`
        """
        return self._interest_type

    @property
    def interest_calculation_type(self):
        """
        :type: :class:`fineract.objects.type.InterestCalculationType`
        """
        return self._interest_calculation_type

    @property
    def transaction_processing_strategy_id(self):
        """
        :type: int
        """
        return self._transaction_processing_strategy_id

    @property
    def transaction_processing_strategy_name(self):
        """
        :type: str
        """
        return self._transaction_processing_strategy_name

    @property
    def principal_variations_for_borrower_cycle(self):
        """
        :type: list
        """
        return self._principal_variations_for_borrower_cycle

    @property
    def interest_rate_variations_for_borrower_cycle(self):
        """
        :type: list
        """
        return self._interest_rate_variations_for_borrower_cycle

    @property
    def number_of_repayment_variations_for_borrower_cycle(self):
        """
        :type: list
        """
        return self._number_of_repayment_variations_for_borrower_cycle

    @property
    def accounting_rule(self):
        """
        :type: :class:`fineract.objects.type.AccountingRule`
        """
        return self._accounting_rule

    @property
    def is_interest_recalculation_enabled(self):
        """
        :type: bool
        """
        return self._is_interest_recalculation_enabled

    @property
    def days_in_year_type(self):
        """
        :type: :class:`fineract.objects.type.DaysInYearType`
        """
        return self._days_in_year_type

    @property
    def days_in_month_type(self):
        """
        :type: :class:`fineract.objects.type.DaysInMonthType`
        """
        return self._days_in_month_type

    @property
    def interest_recalculation_data(self):
        """
        :type: :class:`fineract.objects.interest.InterestRecalculationData`
        """
        return self._interest_recalculation_data

    @property
    def test(self):
        """
        :type:
        """
        return ''

    def _init_attributes(self):
        self._id = None
        self._name = None
        self._short_name = None
        self._include_in_borrower_cycle = None
        self._use_borrower_cycle = None
        self._start_date = None
        self._end_date = None
        self._currency = None
        self._principal = None
        self._min_principal = None
        self._max_principal = None
        self._no_of_repayments = None
        self._min_no_of_repayments = None
        self._max_no_of_repayments = None
        self._repayment_every = None
        self._repayment_frequency_type = None
        self._interest_rate_per_period = None
        self._interest_rate_frequency_type = None
        self._annual_interest_rate = None
        self._amortization_type = None
        self._interest_type = None
        self._interest_calculation_type = None
        self._transaction_processing_strategy_id = None
        self._transaction_processing_strategy_name = None
        self._principal_variations_for_borrower_cycle = None
        self._interest_rate_variations_for_borrower_cycle = None
        self._number_of_repayment_variations_for_borrower_cycle = None
        self._accounting_rule = None
        self._is_interest_recalculation_enabled = None
        self._days_in_year_type = None
        self._days_in_month_type = None
        self._interest_recalculation_data = None

    def _use_attributes(self, attributes):
        self._id = attributes.get('id', None)
        self._name = attributes.get('name', None)
        self._short_name = attributes.get('shortName', None)
        self._include_in_borrower_cycle = attributes.get('includeInBorrowerCycle', None)
        self._use_borrower_cycle = attributes.get('useBorrowerCycle', None)
        self._start_date = self.make_date_object(attributes.get('startDate', None))
        self._close_date = self.make_date_object(attributes.get('closeDate', None))
        self._currency = self.make_fineract_object(Currency, attributes.get('currency', None))
        self._principal = attributes.get('principal', None)
        self._min_principal = attributes.get('minPrincipal', None)
        self._max_principal = attributes.get('maxPrincipal', None)
        self._no_of_repayments = attributes.get('numberOfRepayments', None)
        self._min_no_of_repayments = attributes.get('minNumberOfRepayments', None)
        self._max_of_repayments = attributes.get('maxNumberOfRepayments', None)
        self._repayment_every = attributes.get('repaymentEvery', None)
        self._repayment_frequency_type = self.make_fineract_object(RepaymentFrequencyType,
                                                                   attributes.get('repaymentFrequencyType'))
        self._interest_rate_per_period = attributes.get('interestRateFrequencyType', None)
        self._interest_rate_frequency_type = self.make_fineract_object(InterestFrequencyType,
                                                                       attributes.get('interestRateFrequencyType'))
        self._annual_interest_rate = attributes.get('annualInterestRate', None)
        self._amortization_type = self.make_fineract_object(AmortizationType,
                                                            attributes.get('amortizationType', None))
        self._interest_type = self.make_fineract_object(InterestType,
                                                        attributes.get('interestType', None))
        self._interest_calculation_type = self.make_fineract_object(InterestCalculationPeriodType,
                                                                    attributes.get('interestCalculationPeriodType',
                                                                                   None))
        self._transaction_processing_strategy_id = attributes.get('transactionProcessingStrategyId', None)
        self._transaction_processing_strategy_name = attributes.get('transactionProcessingStrategyName', None)
        self._principal_variations_for_borrower_cycle = attributes.get('principalVariationsForBorrowerCycle', None)
        self._interest_rate_variations_for_borrower_cycle = attributes.get('interestRateVariationsForBorrowerCycle',
                                                                           None)
        self._number_of_repayment_variations_for_borrower_cycle = attributes.get(
            'numberOfRepaymentVariationsForBorrowerCycle', None)
        self._days_in_month_type = self.make_fineract_object(DaysInMonthType, attributes.get('daysInMonthType', None))
        self._days_in_year_type = self.make_fineract_object(DaysInYearType, attributes.get('daysInYearType', None))
        self._is_interest_recalculation_enabled = attributes.get('isInterestRecalculationEnabled', None)
        self._accounting_rule = self.make_fineract_object(AccountingRule, attributes.get('accountingRule', None))
        self._interest_recalculation_data = self.make_fineract_object(InterestRecalculationData,
                                                                      attributes.get('interestRecalculationData', None))
