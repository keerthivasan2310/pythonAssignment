import unittest
import sys
import os

# Standard path hack to reach src/timedelta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/timedelta')))

from util import get_time_delta

class TestTimeDelta(unittest.TestCase):
    def test_case_0(self):
        # Sample Input 0 - Case 1
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(get_time_delta(t1, t2), "25200")

    def test_case_1(self):
        # Sample Input 0 - Case 2
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        self.assertEqual(get_time_delta(t1, t2), "88200")

if __name__ == "__main__":
    unittest.main()