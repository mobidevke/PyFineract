from fineract.objects.fineract_object import FineractObject


class Type(FineractObject):

    def __repr__(self):
        return self.get__repr__({'value': self._value})

    @property
    def id(self):
        return self._id

    @property
    def code(self):
        return self._code

    @property
    def value(self):
        return self._value

    def _init_attributes(self):
        self._id = None
        self._code = None
        self._value = None

    def _use_attributes(self, attributes):
        self._id = attributes.get('id', None)
        self._code = attributes.get('code', None)
        self._value = attributes.get('value', None)


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
