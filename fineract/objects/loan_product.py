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
        return self.get__repr__({'short_name': self.short_name})

    def _init_attributes(self):
        self.id = None
        self.name = None
        self.short_name = None
        self.include_in_borrower_cycle = None
        self.use_borrower_cycle = None
        self.start_date = None
        self.end_date = None
        self.currency = None
        self.principal = None
        self.min_principal = None
        self.max_principal = None
        self.no_of_repayments = None
        self.min_no_of_repayments = None
        self.max_no_of_repayments = None
        self.repayment_every = None
        self.repayment_frequency_type = None
        self.interest_rate_per_period = None
        self.interest_rate_frequency_type = None
        self.annual_interest_rate = None
        self.amortization_type = None
        self.interest_type = None
        self.interest_calculation_type = None
        self.transaction_processing_strategy_id = None
        self.transaction_processing_strategy_name = None
        self.principal_variations_for_borrower_cycle = None
        self.interest_rate_variations_for_borrower_cycle = None
        self.number_of_repayment_variations_for_borrower_cycle = None
        self.accounting_rule = None
        self.is_interest_recalculation_enabled = None
        self.days_in_year_type = None
        self.days_in_month_type = None
        self.interest_recalculation_data = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.short_name = attributes.get('shortName', None)
        self.include_in_borrower_cycle = attributes.get('includeInBorrowerCycle', None)
        self.use_borrower_cycle = attributes.get('useBorrowerCycle', None)
        self.start_date = self._make_date_object(attributes.get('startDate', None))
        self.close_date = self._make_date_object(attributes.get('closeDate', None))
        self.currency = self._make_fineract_object(Currency, attributes.get('currency', None))
        self.principal = attributes.get('principal', None)
        self.min_principal = attributes.get('minPrincipal', None)
        self.max_principal = attributes.get('maxPrincipal', None)
        self.no_of_repayments = attributes.get('numberOfRepayments', None)
        self.min_no_of_repayments = attributes.get('minNumberOfRepayments', None)
        self.max_of_repayments = attributes.get('maxNumberOfRepayments', None)
        self.repayment_every = attributes.get('repaymentEvery', None)
        self.repayment_frequency_type = self._make_fineract_object(RepaymentFrequencyType,
                                                                   attributes.get('repaymentFrequencyType'))
        self.interest_rate_per_period = attributes.get('interestRateFrequencyType', None)
        self._interest_rate_frequency_type = self._make_fineract_object(InterestFrequencyType,
                                                                        attributes.get('interestRateFrequencyType'))
        self.annual_interest_rate = attributes.get('annualInterestRate', None)
        self.amortization_type = self._make_fineract_object(AmortizationType,
                                                            attributes.get('amortizationType', None))
        self.interest_type = self._make_fineract_object(InterestType,
                                                        attributes.get('interestType', None))
        self.interest_calculation_type = self._make_fineract_object(InterestCalculationPeriodType,
                                                                    attributes.get('interestCalculationPeriodType',
                                                                                   None))
        self.transaction_processing_strategy_id = attributes.get('transactionProcessingStrategyId', None)
        self.transaction_processing_strategy_name = attributes.get('transactionProcessingStrategyName', None)
        self.principal_variations_for_borrower_cycle = attributes.get('principalVariationsForBorrowerCycle', None)
        self.interest_rate_variations_for_borrower_cycle = attributes.get('interestRateVariationsForBorrowerCycle',
                                                                           None)
        self.number_of_repayment_variations_for_borrower_cycle = attributes.get(
            'numberOfRepaymentVariationsForBorrowerCycle', None)
        self.days_in_month_type = self._make_fineract_object(DaysInMonthType, attributes.get('daysInMonthType', None))
        self.days_in_year_type = self._make_fineract_object(DaysInYearType, attributes.get('daysInYearType', None))
        self.is_interest_recalculation_enabled = attributes.get('isInterestRecalculationEnabled', None)
        self.accounting_rule = self._make_fineract_object(AccountingRule, attributes.get('accountingRule', None))
        self.interest_recalculation_data = self._make_fineract_object(InterestRecalculationData,
                                                                      attributes.get('interestRecalculationData', None))
