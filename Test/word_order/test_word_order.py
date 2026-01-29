import unittest
import sys
import os

# Standard path hack to reach src/word_order
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/word_order')))

from util import get_word_stats

class TestWordOrder(unittest.TestCase):
    def test_sample_case(self):
        # Sample input words
        words = ["bcdef", "abcdefg", "bcde", "bcdef"]
        
        distinct_count, occurrences = get_word_stats(words)
        
        # Expected: 3 distinct words with counts 2, 1, 1
        self.assertEqual(distinct_count, 3)
        self.assertEqual(occurrences, [2, 1, 1])

    def test_single_word(self):
        words = ["apple", "apple", "apple"]
        distinct_count, occurrences = get_word_stats(words)
        self.assertEqual(distinct_count, 1)
        self.assertEqual(occurrences, [3])

if __name__ == "__main__":
    unittest.main()