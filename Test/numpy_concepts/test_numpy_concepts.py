import unittest
import sys
import os
import numpy

# Path hack to reach src/numpy_stats
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/numpy_stats')))

from util import get_numpy_stats

class TestNumpyStats(unittest.TestCase):
    def test_sample_input(self):
        # Sample case from the challenge: 2x2 matrix
        data = [[1, 2], [3, 4]]
        
        mean_res, var_res, std_res = get_numpy_stats(data)
        
        # Expected outputs based on sample
        # Mean axis 1: [1.5, 3.5]
        # Var axis 0: [1.0, 1.0]
        # Std axis None: 1.11803398875
        numpy.testing.assert_array_equal(mean_res, [1.5, 3.5])
        numpy.testing.assert_array_equal(var_res, [1.0, 1.0])
        self.assertAlmostEqual(std_res, 1.11803398875, places=10)

if __name__ == "__main__":
    unittest.main()