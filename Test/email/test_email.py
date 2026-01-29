import unittest
import sys
import os

# Standard path hack
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/email_filter')))

from util import is_valid_email, filter_emails

class TestEmailFilter(unittest.TestCase):
    def test_validation_rules(self):
        # Valid cases
        self.assertTrue(is_valid_email("lara@hackerrank.com"))
        self.assertTrue(is_valid_email("brian-23@hackerrank.com"))
        
        # Invalid cases
        self.assertFalse(is_valid_email("wrong@format@test.com")) # Too many @
        self.assertFalse(is_valid_email("user@web.extension"))    # Extension too long (>3)
        self.assertFalse(is_valid_email("user#name@web.com"))     # Invalid char in username

    def test_sample_case(self):
        emails = ["lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com"]
        expected = ["brian-23@hackerrank.com", "britts_54@hackerrank.com", "lara@hackerrank.com"]
        self.assertEqual(filter_emails(emails), expected)

if __name__ == "__main__":
    unittest.main()