import unittest
import sys
import os

# Standard path hack
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/iterables')))

from util import calculate_probability

class TestIterables(unittest.TestCase):
    def test_sample_case(self):
        # Sample input: 4, ['a', 'a', 'c', 'd'], 2
        # Total combinations: (1,2), (1,3), (1,4), (2,3), (2,4), (3,4) = 6
        # Favorable: (1,2), (1,3), (1,4), (2,3), (2,4) = 5
        # 5/6 = 0.8333...
        n = 4
        letters = ['a', 'a', 'c', 'd']
        k = 2
        self.assertAlmostEqual(calculate_probability(n, letters, k), 0.8333333333, places=4)

    def test_no_a_present(self):
        # If 'a' isn't there, probability should be 0
        self.assertEqual(calculate_probability(3, ['b', 'c', 'd'], 1), 0.0)

if __name__ == "__main__":
    unittest.main()