from fineract.objects.fineract_object import FineractObject
from fineract.objects.types import InterestRecalculationCompoundingType, RecalculationCompoundingFrequencyType, \
    RescheduleStrategyType, RecalculationRestFrequencyType, PreClosureInterestCalculationStrategy


class InterestRecalculationData(FineractObject):
    """
    This class represents InterestRecalculationData
    """

    @property
    def id(self):
        """
        :type: int
        """
        return self._id

    @property
    def product_id(self):
        """
        :type: int
        """
        return self._product_id

    @property
    def interest_recalculation_compounding_type(self):
        return self._interest_recalculation_compounding_type

    @property
    def recalculation_compounding_frequency_type(self):
        return self._recalculation_compounding_frequency_type

    @property
    def reschedule_strategy_type(self):
        return self._reschedule_strategy_type

    @property
    def recalculation_rest_frequency_type(self):
        return self._recalculation_rest_frequency_type

    @property
    def pre_closure_interest_calculation_strategy(self):
        return self._pre_closure_interest_calculation_strategy

    @property
    def is_arrears_based_on_original_schedule(self):
        """
        :type: bool
        """
        return self._is_arrears_based_on_original_schedule

    def _init_attributes(self):
        self._id = None
        self._product_id = None
        self._interest_recalculation_compounding_type = None
        self._recalculation_compounding_frequency_type = None
        self._reschedule_strategy_type = None
        self._recalculation_rest_frequency_type = None
        self._pre_closure_interest_calculation_strategy = None
        self._is_arrears_based_on_original_schedule = None

    def _use_attributes(self, attributes):
        self._id = attributes.get('id', None)
        self._product_id = attributes.get('productId', None)

        self._interest_recalculation_compounding_type = self.make_fineract_object(InterestRecalculationCompoundingType,
                                                                                  attributes.get(
                                                                                      'interestRecalculationCompoundingType',
                                                                                      None))
        self._recalculation_compounding_frequency_type = self.make_fineract_object(
            RecalculationCompoundingFrequencyType,
            attributes.get('recalculationCompoundingFrequencyType', None))
        self._reschedule_strategy_type = self.make_fineract_object(RescheduleStrategyType,
                                                                   attributes.get('rescheduleStrategyType', None))
        self._recalculation_rest_frequency_type = self.make_fineract_object(RecalculationRestFrequencyType,
                                                                            attributes.get(
                                                                                'recalculationRestFrequencyType', None))
        self._pre_closure_interest_calculation_strategy = self.make_fineract_object(
            PreClosureInterestCalculationStrategy,
            attributes.get('preClosureInterestCalculationStrategy', None))
        self._is_arrears_based_on_original_schedule = attributes.get('isArrearsBasedOnOriginalSchedule', None)
