import json

from fineract.objects.interest import InterestRecalculationData
from fineract.objects.types import InterestRecalculationCompoundingType, RecalculationCompoundingFrequencyType, \
    RescheduleStrategyType, RecalculationRestFrequencyType, PreClosureInterestCalculationStrategy


def test_currency_creation():
    with open('tests/files/interest_recalculation_data.json', 'r') as in_file:
        data = json.load(in_file)
        irc = InterestRecalculationData(None, data, False)
        assert isinstance(irc.interest_recalculation_compounding_type, InterestRecalculationCompoundingType)
        assert isinstance(irc.recalculation_compounding_frequency_type, RecalculationCompoundingFrequencyType)
        assert isinstance(irc.reschedule_strategy_type, RescheduleStrategyType)
        assert isinstance(irc.recalculation_rest_frequency_type, RecalculationRestFrequencyType)
        assert isinstance(irc.pre_closure_interest_calculation_strategy, PreClosureInterestCalculationStrategy)
        assert irc.is_arrears_based_on_original_schedule
        assert irc.id == 3
        assert irc.product_id == 1
