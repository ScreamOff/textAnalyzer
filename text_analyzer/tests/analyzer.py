import csv  # Importujemy moduł csv do obsługi plików CSV
from collections import Counter  # Importujemy klasę Counter z modułu collections do zliczania elementów

# Definiujemy klasę TextAnalyzer
class TextAnalyzer:
    # Inicjalizator klasy przyjmuje nazwę pliku jako argument
    def __init__(self, filename):
        self.filename = filename  # Przechowujemy nazwę pliku w atrybucie instancji
        self.text = self._load_text()  # Ładujemy tekst z pliku i przechowujemy go w atrybucie instancji

    # Prywatna metoda do ładowania tekstu z pliku
    def _load_text(self):
        # Otwieramy plik w trybie odczytu i kodowaniu UTF-8
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()  # Zwracamy zawartość pliku jako tekst

    # Metoda licząca liczbę słów w tekście
    def word_count(self):
        words = self.text.split()  # Dzielimy tekst na słowa
        return len(words)  # Zwracamy liczbę słów

    # Metoda zwracająca najczęściej występujące słowa
    def most_common_words(self, n=10):
        words = self.text.split()  # Dzielimy tekst na słowa
        word_freq = Counter(words)  # Liczymy częstotliwość występowania słów
        return word_freq.most_common(n)  # Zwracamy n najczęściej występujących słów

    # Metoda zapisująca wyniki do pliku CSV
    def save_results(self, output_file):
        word_freq = self.most_common_words()  # Pobieramy najczęściej występujące słowa
        # Otwieramy plik CSV w trybie zapisu
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)  # Tworzymy obiekt writer do zapisu CSV
            writer.writerow(['Word', 'Frequency'])  # Zapisujemy nagłówki kolumn
            # Zapisujemy każdą parę (słowo, częstotliwość)
            for word, freq in word_freq:
                writer.writerow([word, freq])
