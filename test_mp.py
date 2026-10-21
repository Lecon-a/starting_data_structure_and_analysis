
import unittest
from miniproject1 import seq_analyzer


class TestSequenceAnalyzer(unittest.TestCase):

    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            seq_analyzer([])

    def test_single_element_sequence(self):
        result = seq_analyzer([5])

        expected = {
            "mx_num": 5,
            "mn_num": 5,
            "_sum": 5,
            "avg": 5,
            "positive_count": 1,
            "negative_count": 0,
            "zero_count": 0
        }

        self.assertEqual(result, expected)

    def test_all_negative_numbers(self):
        result = seq_analyzer([-4, -9, -2, -7])

        self.assertEqual(result["mx_num"], -2)
        self.assertEqual(result["mn_num"], -9)
        self.assertEqual(result["_sum"], -22)
        self.assertEqual(result["avg"], -5.5)
        self.assertEqual(result["positive_count"], 0)
        self.assertEqual(result["negative_count"], 4)
        self.assertEqual(result["zero_count"], 0)

    def test_all_positive_numbers(self):
        result = seq_analyzer([2, 5, 8, 10])

        self.assertEqual(result["mx_num"], 10)
        self.assertEqual(result["mn_num"], 2)
        self.assertEqual(result["_sum"], 25)
        self.assertEqual(result["avg"], 6.25)
        self.assertEqual(result["positive_count"], 4)
        self.assertEqual(result["negative_count"], 0)
        self.assertEqual(result["zero_count"], 0)

    def test_all_zeros(self):
        result = seq_analyzer([0, 0, 0, 0])

        self.assertEqual(result["mx_num"], 0)
        self.assertEqual(result["mn_num"], 0)
        self.assertEqual(result["_sum"], 0)
        self.assertEqual(result["avg"], 0)
        self.assertEqual(result["positive_count"], 0)
        self.assertEqual(result["negative_count"], 0)
        self.assertEqual(result["zero_count"], 4)

    def test_duplicate_values(self):
        result = seq_analyzer([2, 5, 5, 1])

        self.assertEqual(result["mx_num"], 5)
        self.assertEqual(result["mn_num"], 1)
        self.assertEqual(result["_sum"], 13)
        self.assertEqual(result["avg"], 3.25)
        self.assertEqual(result["positive_count"], 4)
        self.assertEqual(result["negative_count"], 0)
        self.assertEqual(result["zero_count"], 0)

    def test_mixed_positive_negative_and_zero(self):
        result = seq_analyzer([-3, 0, 5, -1, 2])

        self.assertEqual(result["mx_num"], 5)
        self.assertEqual(result["mn_num"], -3)
        self.assertEqual(result["_sum"], 3)
        self.assertAlmostEqual(result["avg"], 0.6)
        self.assertEqual(result["positive_count"], 2)
        self.assertEqual(result["negative_count"], 2)
        self.assertEqual(result["zero_count"], 1)

    def test_decimal_values(self):
        result = seq_analyzer([1.5, -2.5, 0.0])

        self.assertEqual(result["mx_num"], 1.5)
        self.assertEqual(result["mn_num"], -2.5)
        self.assertEqual(result["_sum"], -1.0)
        self.assertAlmostEqual(result["avg"], -1 / 3)
        self.assertEqual(result["positive_count"], 1)
        self.assertEqual(result["negative_count"], 1)
        self.assertEqual(result["zero_count"], 1)

    def test_large_numbers(self):
        numbers = [10**100, -(10**100), 5]
        result = seq_analyzer(numbers)

        self.assertEqual(result["mx_num"], 10**100)
        self.assertEqual(result["mn_num"], -(10**100))
        self.assertEqual(result["_sum"], 5)
        self.assertEqual(result["avg"], 5 / 3)
        self.assertEqual(result["positive_count"], 2)
        self.assertEqual(result["negative_count"], 1)
        self.assertEqual(result["zero_count"], 0)


if __name__ == "__main__":
    unittest.main()
