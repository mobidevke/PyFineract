from fineract.objects.currency import Currency
from fineract.objects.fineract_object import FineractObject
from fineract.objects.types import ChargeTimeType, ChargeAppliesTo, ChargeCalculationType, ChargePaymentMode


class Office(FineractObject):
    """
    This class represent an Office
    """

    def _init_attributes(self):
        self.id = None
        self.name = None
        self.name_decorated = None
        self.external_id = None
        self.opening_date = None
        self.hierarchy = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.name_decorated = attributes.get('nameDecorated', None)
        self.external_id = attributes.get('externalId', None)
        self.opening_date = self._make_date_object(attributes.get('openingDate', None))
        self.hierarchy = attributes.get('hierarchy', None)


class Staff(FineractObject):
    """
    This class represents a Staff
    """

    def _init_attributes(self):
        self.id = None
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
        self.id = attributes.get('id', None)
        self.firstname = attributes.get('firstname', None)
        self.lastname = attributes.get('lastname', None)
        self.display_name = attributes.get('displayName', None)
        self.office_id = attributes.get('officeId', None)
        self.office_name = attributes.get('officeName', None)
        self.is_loan_officer = attributes.get('isLoanOfficer', None)
        self.is_active = attributes.get('externalId', None)
        self.join_date = self._make_date_object(attributes.get('joiningDate', None))


class Fund(FineractObject):
    """
    This class represents a Fund
    """

    def _init_attributes(self):
        self.id = None
        self.name = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)


class Charge(FineractObject):
    """
    This class represents a Charge
    """

    def _init_attributes(self):
        self.id = None
        self.name = None
        self.active = None
        self.penalty = None
        self.currency = None
        self.amount = None
        self.charge_time_type = None
        self.charge_applies_to = None
        self.charge_calculation_type = None
        self.charge_payment_mode = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.active = attributes.get('active', None)
        self.penalty = attributes.get('penalty', None)
        self.currency = self._make_fineract_object(Currency, attributes.get('currency', None))
        self.amount = attributes.get('amount', None)
        self.charge_time_type = self._make_fineract_object(ChargeTimeType, attributes.get('chargeTimeType', None))
        self.charge_applies_to = self._make_fineract_object(ChargeAppliesTo, attributes.get('chargeAppliesTo', None))
        self.charge_calculation_type = self._make_fineract_object(ChargeCalculationType,
                                                                  attributes.get('chargeCalculationType', None))
        self.charge_payment_mode = self._make_fineract_object(ChargePaymentMode,
                                                              attributes.get('chargePaymentMode', None))
