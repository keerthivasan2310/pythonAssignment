import unittest
import sys
import os

# Path hack to reach src/student
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/student')))

from util import calculate_average

class TestStudentAverage(unittest.TestCase):
    def test_case_01(self):
        n = 5
        cols = ['ID', 'MARKS', 'NAME', 'CLASS']
        data = [
            "1 97 Raymond 7",
            "2 50 Steven 4",
            "3 91 Adrian 9",
            "4 72 Stewart 5",
            "5 80 Peter 6"
        ]
        self.assertAlmostEqual(calculate_average(n, cols, data), 78.00)

    def test_case_02(self):
        n = 5
        cols = ['MARKS', 'CLASS', 'NAME', 'ID']
        data = [
            "92 2 Calum 1",
            "82 5 Scott 2",
            "94 2 Jason 3",
            "55 8 Glenn 4",
            "82 2 Fergus 5"
        ]
        self.assertAlmostEqual(calculate_average(n, cols, data), 81.00)

if __name__ == "__main__":
    unittest.main()