from cgitb import text
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import unittest
import textbox

class Test(unittest.TestCase):
    def test_incorrectMazeTooManyPersons(self):
        self.assertTrue(textbox.textVar)

if __name__ == '__main__':
    unittest.main()