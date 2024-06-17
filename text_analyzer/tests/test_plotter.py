import sys  # Importujemy moduł sys do manipulowania ścieżkami systemowymi
import os  # Importujemy moduł os do operacji na plikach i ścieżkach
import unittest  # Importujemy moduł unittest do pisania testów jednostkowych
from plotter import Plotter  # Importujemy klasę Plotter z modułu plotter

# Dodajemy katalog nadrzędny do ścieżki systemowej, aby móc importować moduły z wyższych poziomów katalogów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Definiujemy klasę testową dla Plotter
class TestPlotter(unittest.TestCase):
    # Test funkcjonalny dla metody plot_word_frequency
    def test_plot_creation(self):
        data = [('Maciek', 200), ('Daniel', 100)]  # Przykładowe dane do wykresu
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Ustalanie ścieżki bazowej
        plotter = Plotter(data)  # Tworzenie instancji Plotter z przykładowymi danymi
        plotter.plot_word_frequency(os.path.join(base_path, 'data', 'test_word_frequency.svg'))  # Tworzenie wykresu i zapisywanie go do pliku SVG

# Uruchamiamy testy, jeśli skrypt jest wykonywany bezpośrednio
if __name__ == '__main__':
    unittest.main()
