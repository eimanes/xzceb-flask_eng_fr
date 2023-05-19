import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from translator import french_to_english, english_to_french

class TestTranslationFunctions(unittest.TestCase):

    def test_null_input_english_to_french(self):
        with self.assertRaises(ValueError):
            english_to_french(None)

    def test_null_input_french_to_english(self):
        with self.assertRaises(ValueError):
            french_to_english(None)

    def test_hello_to_bonjour(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_bonjour_to_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()

