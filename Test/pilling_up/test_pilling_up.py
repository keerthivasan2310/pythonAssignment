import unittest
import sys
import os

# Standard path hack
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/piling_up')))

from util import can_stack_cubes

class TestPilingUp(unittest.TestCase):
    def test_sample_yes(self):
        # Sample Case 1: [4, 3, 2, 1, 3, 4] -> Yes
        # You can pick 4, then 4, then 3, then 3, etc.
        self.assertEqual(can_stack_cubes([4, 3, 2, 1, 3, 4]), "Yes")

    def test_sample_no(self):
        # Sample Case 2: [1, 3, 2] -> No
        # Pick 2, then 1... then 3 is larger than 1. Fail.
        self.assertEqual(can_stack_cubes([1, 3, 2]), "No")

    def test_all_equal(self):
        self.assertEqual(can_stack_cubes([5, 5, 5]), "Yes")

if __name__ == "__main__":
    unittest.main()