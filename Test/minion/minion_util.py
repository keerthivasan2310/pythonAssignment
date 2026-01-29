import unittest
import sys
import os

# Add the src/minion directory to the path so we can import util
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/minion')))

from util import minion_game
from io import StringIO

class TestMinionGame(unittest.TestCase):
    def test_sample_case(self):
        # Capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        minion_game("BANANA")
        
        sys.stdout = sys.__stdout__ # Reset redirect
        self.assertEqual(captured_output.getvalue().strip(), "Stuart 12")

if __name__ == "__main__":
    unittest.main()