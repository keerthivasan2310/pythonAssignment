import unittest
import sys
import os

# Standard path hack
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/no_idea')))

from util import calculate_happiness

class TestNoIdea(unittest.TestCase):
    def test_sample_case(self):
        # Sample Input: 
        # Array: [1, 5, 3]
        # Set A: {3, 1}
        # Set B: {5, 7}
        n_array = [1, 5, 3]
        set_a = {3, 1}
        set_b = {5, 7}
        
        # (1 in A: +1) + (5 in B: -1) + (3 in A: +1) = 1
        self.assertEqual(calculate_happiness(n_array, set_a, set_b), 1)

    def test_no_overlap(self):
        n_array = [10, 20, 30]
        set_a = {1, 2}
        set_b = {3, 4}
        self.assertEqual(calculate_happiness(n_array, set_a, set_b), 0)

if __name__ == "__main__":
    unittest.main()
    