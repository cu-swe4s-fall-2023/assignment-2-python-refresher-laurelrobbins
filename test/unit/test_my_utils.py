import unittest
import my_utils
import random
import statistics
import sys

sys.path.insert(0, '../../src')

a = random.randint(-100, 100)
b = random.randint(-100, 100)
c = random.randint(-100, 100)


class TestCalc(unittest.TestCase):

    def test_mean_equal(self):
        r = (a + b) / 2
        self.assertEqual(my_utils.mean([a, b]), r)

    def test_mean_one(self):
        self.assertNotEqual(my_utils.mean([a, a, a]), [a + 1])

    def test_mean_neg(self):
        self.assertLess(my_utils.mean([-1, -2, -3]), 0)

    def test_median_equal(self):
        self.assertEqual(my_utils.median([a, b, a]), a)

    def test_median_not_equal(self):
        self.assertNotEqual(my_utils.median([a, a, a]), (a + 1))

    def test_median_empty_list(self):
        self.assertIsNone(my_utils.median([]))

    def test_std_dev_equal(self):
        my_std_dev = my_utils.std_dev([a, b, c])
        compared_std_dev = statistics.stdev([a, b, c])
        # Almost equal accounts for differences in floating point numbers
        self.assertAlmostEqual(my_std_dev, compared_std_dev, places=6)

    def test_std_dev_more(self):
        self.assertGreater(my_utils.std_dev([a, b, c]), 0)

    def test_std_dev_empty_list(self):
        self.assertIsNone(my_utils.std_dev([]))

    def second_way_of_testing_empty_array(self):
        self.assertEqual(my_utils.std_dev([]), None)
