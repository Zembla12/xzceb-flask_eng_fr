import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_hello_to_french(self):
        # Test translation of 'Hello' to French
        english_text = "Hello"
        expected_french_text = "Bonjour"
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, expected_french_text)

    def test_bonjour_to_english(self):
        # Test translation of 'Bonjour' to English
        french_text = "Bonjour"
        expected_english_text = "Hello"
        english_text = french_to_english(french_text)
        self.assertEqual(english_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()
