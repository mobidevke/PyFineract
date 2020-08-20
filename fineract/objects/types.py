from fineract.objects.fineract_object import FineractObject


class Type(FineractObject):

    def __repr__(self):
        return self.get__repr__({'value': self.value})

    def _init_attributes(self):
        self.id = None
        self.code = None
        self.value = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.code = attributes.get('code', None)
        self.value = attributes.get('value', None)


class RepaymentFrequencyType(Type):
    pass


class InterestFrequencyType(Type):
    pass


class AmortizationType(Type):
    pass


class InterestType(Type):
    pass


class InterestCalculationPeriodType(Type):
    pass


class DaysInMonthType(Type):
    pass


class DaysInYearType(Type):
    pass


class AccountingRule(Type):
    pass


class InterestRecalculationCompoundingType(Type):
    pass


class RecalculationCompoundingFrequencyType(Type):
    pass


class RescheduleStrategyType(Type):
    pass


class RecalculationRestFrequencyType(Type):
    pass


class PreClosureInterestCalculationStrategy(Type):
    pass


class LoanType(Type):
    pass


class TermPeriodFrequencyType(Type):
    pass


class ChargeTimeType(Type):
    pass


class ChargeAppliesTo(Type):
    pass


class ChargeCalculationType(Type):
    pass


class ChargePaymentMode(Type):
    pass
