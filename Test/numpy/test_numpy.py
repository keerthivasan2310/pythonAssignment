import unittest
import sys
import os
import numpy

# Path hack to reach src/numpy_ops
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/numpy_ops')))

from util import get_numpy_math_ops

class TestNumpyMath(unittest.TestCase):
    def test_sample_input(self):
        input_data = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
        floor_res, ceil_res, rint_res = get_numpy_math_ops(input_data)
        
        # Check if values match expected results
        expected_floor = [1., 2., 3., 4., 5., 6., 7., 8., 9.]
        expected_ceil = [2., 3., 4., 5., 6., 7., 8., 9., 10.]
        expected_rint = [1., 2., 3., 4., 6., 7., 8., 9., 10.]
        
        numpy.testing.assert_array_equal(floor_res, expected_floor)
        numpy.testing.assert_array_equal(ceil_res, expected_ceil)
        numpy.testing.assert_array_equal(rint_res, expected_rint)

if __name__ == "__main__":
    unittest.main()