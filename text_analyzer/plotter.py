import matplotlib.pyplot as plt  # Importujemy bibliotekę do tworzenia wykresów

# Definiujemy klasę Plotter
class Plotter:
    # Inicjalizator klasy przyjmuje dane jako argument
    def __init__(self, data):
        self.data = data  # Przechowujemy dane w atrybucie instancji

    # Metoda do rysowania wykresu częstotliwości słów i zapisywania go do pliku
    def plot_word_frequency(self, output_file):
        words, frequencies = zip(*self.data)  # Rozpakowujemy dane na słowa i częstotliwości
        plt.figure(figsize=(10, 8))  # Tworzymy nową figurę o wymiarach 10x8 cali
        plt.bar(words, frequencies, color='blue')  # Rysujemy wykres słupkowy
        plt.xlabel('Words')  # Ustawiamy etykietę osi X
        plt.ylabel('Frequency')  # Ustawiamy etykietę osi Y
        plt.title('Top Word Frequencies')  # Ustawiamy tytuł wykresu
        plt.xticks(rotation=45)  # Obracamy etykiety osi X o 45 stopni, aby były czytelniejsze
        plt.tight_layout()  # Automatycznie dostosowujemy układ, aby uniknąć nakładania się elementów
        plt.savefig(output_file)  # Zapisujemy wykres do pliku o podanej nazwie
