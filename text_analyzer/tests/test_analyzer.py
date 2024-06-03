import sys
import os
import unittest
from analyzer import TextAnalyzer

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.analyzer = TextAnalyzer(os.path.join(base_path, 'data', 'input.txt'))

    def test_word_count(self):
        self.assertEqual(self.analyzer.word_count(), 7)

    def test_most_common_words(self):
        result = self.analyzer.most_common_words(2)
        self.assertEqual(result[0][0], 'ma')
        self.assertEqual(result[0][1], 2)

if __name__ == '__main__':
    unittest.main()
