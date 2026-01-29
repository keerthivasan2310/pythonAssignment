import unittest
from util import get_day_of_week

class TestCalendarModule(unittest.TestCase):

    def test_sample_input(self):
        # Testing the example from the HackerRank challenge
        self.assertEqual(get_day_of_week(8, 5, 2015), "WEDNESDAY")

    def test_known_dates(self):
        # Testing other known dates
        self.assertEqual(get_day_of_week(1, 1, 2024), "MONDAY")
        self.assertEqual(get_day_of_week(12, 25, 2023), "MONDAY")
        self.assertEqual(get_day_of_week(7, 4, 1776), "THURSDAY")

if __name__ == "__main__":
    unittest.main()