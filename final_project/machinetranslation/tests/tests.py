import unittest
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestNullInput(unittest.TestCase):
    def test_frenchToEnglish_null_input(self):
        self.assertEqual(french_to_english(), null)

    def test_englishToFrench_null_input(self):
        self.assertEqual(english_to_french(), null)

unittest.main()