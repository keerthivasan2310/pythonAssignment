import unittest
import sys
import os

# Path hack to reach src/min_max
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/min_max')))

from util import get_min_max_result

class TestMinMax(unittest.TestCase):
    def test_sample_input(self):
        # Sample case from the challenge
        n, m = 4, 2
        data = [
            [2, 5],
            [3, 7],
            [1, 3],
            [4, 0]
        ]
        # Min along axis 1 = [2, 3, 1, 0]. Max of that = 3.
        self.assertEqual(get_min_max_result(n, m, data), 3)

if __name__ == "__main__":
    unittest.main()