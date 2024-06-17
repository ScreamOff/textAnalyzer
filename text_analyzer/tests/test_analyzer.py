import sys  # Importujemy moduł sys do manipulowania ścieżkami systemowymi
import os  # Importujemy moduł os do operacji na plikach i ścieżkach
import unittest  # Importujemy moduł unittest do pisania testów jednostkowych
from analyzer import TextAnalyzer  # Importujemy klasę TextAnalyzer z modułu analyzer

# Dodajemy katalog nadrzędny do ścieżki systemowej, aby móc importować moduły z wyższych poziomów katalogów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Definiujemy klasę testową dla TextAnalyzer
class TestTextAnalyzer(unittest.TestCase):
    # Metoda setUp uruchamia się przed każdym testem
    def setUp(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Ustalanie ścieżki bazowej
        self.analyzer = TextAnalyzer(os.path.join(base_path, 'data', 'input.txt'))  # Tworzenie instancji TextAnalyzer z plikiem input.txt

    # Test jednostkowy dla metody word_count
    def test_word_count(self):
        self.assertEqual(self.analyzer.word_count(), 7)  # Sprawdzamy, czy liczba słów wynosi 7

    # Test wybiorczy dla metody most_common_words
    def test_most_common_words(self):
        result = self.analyzer.most_common_words(2)  # Pobieramy 2 najczęściej występujące słowa
        self.assertEqual(result[0][0], 'ma')  # Sprawdzamy, czy najczęściej występującym słowem jest 'ma'
        self.assertEqual(result[0][1], 2)  # Sprawdzamy, czy słowo 'ma' występuje 2 razy

# Uruchamiamy testy, jeśli skrypt jest wykonywany bezpośrednio
if __name__ == '__main__':
    unittest.main()
