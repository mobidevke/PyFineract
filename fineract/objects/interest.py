from fineract.objects.fineract_object import FineractObject
from fineract.objects.types import InterestRecalculationCompoundingType, RecalculationCompoundingFrequencyType, \
    RescheduleStrategyType, RecalculationRestFrequencyType, PreClosureInterestCalculationStrategy


class InterestRecalculationData(FineractObject):
    """
    This class represents InterestRecalculationData
    """

    def _init_attributes(self):
        self.id = None
        self.product_id = None
        self.interest_recalculation_compounding_type = None
        self.recalculation_compounding_frequency_type = None
        self.reschedule_strategy_type = None
        self.recalculation_rest_frequency_type = None
        self.pre_closure_interest_calculation_strategy = None
        self.is_arrears_based_on_original_schedule = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.product_id = attributes.get('productId', None)

        self.interest_recalculation_compounding_type = self._make_fineract_object(InterestRecalculationCompoundingType,
                                                                                  attributes.get(
                                                                                      'interestRecalculationCompoundingType',
                                                                                      None))
        self.recalculation_compounding_frequency_type = self._make_fineract_object(
            RecalculationCompoundingFrequencyType,
            attributes.get('recalculationCompoundingFrequencyType', None))
        self.reschedule_strategy_type = self._make_fineract_object(RescheduleStrategyType,
                                                                   attributes.get('rescheduleStrategyType', None))
        self.recalculation_rest_frequency_type = self._make_fineract_object(RecalculationRestFrequencyType,
                                                                            attributes.get(
                                                                                'recalculationRestFrequencyType', None))
        self.pre_closure_interest_calculation_strategy = self._make_fineract_object(
            PreClosureInterestCalculationStrategy,
            attributes.get('preClosureInterestCalculationStrategy', None))
        self.is_arrears_based_on_original_schedule = attributes.get('isArrearsBasedOnOriginalSchedule', None)
