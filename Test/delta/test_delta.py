import unittest
import sys
import os

# Path hack to reach src/timedelta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/timedelta')))

from util import time_delta

class TestTimeDelta(unittest.TestCase):
    def test_sample_case_0(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), 25200)

    def test_sample_case_1(self):
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), 88200)

if __name__ == "__main__":
    unittest.main()