from unittest import TestCase
from libs.calculators.total_dict import TotalDictCalculator


class TestTotalDictCalculator(TestCase):

    def test_calculate(self):
        calculator = TotalDictCalculator([
            {
                "field_1": 8,
                "field_2": 2,
                "field_str": "Hello"
            },
            {
                "field_1": 3,
                "field_2": 10,
                "field_str": "Hello"
            }
        ])

        self.assertDictEqual(
            calculator.calculate(),
            {
                "field_1": 11,
                "field_2": 12,
                "field_str": "---"
            }
        )
