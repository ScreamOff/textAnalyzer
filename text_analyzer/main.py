from analyzer import TextAnalyzer  # Importujemy klasę TextAnalyzer z modułu analyzer
from plotter import Plotter  # Importujemy klasę Plotter z modułu plotter
from colorama import Fore, init  # Importujemy funkcje i stałe z biblioteki colorama do kolorowania tekstu w terminalu

# Definiujemy główną funkcję programu
def main():
    init(autoreset=True)  # Inicjalizujemy coloramę z automatycznym resetowaniem kolorów po każdym użyciu

    input_file = 'data/input.txt'  # Ścieżka do pliku wejściowego z tekstem
    output_csv = 'data/output.csv'  # Ścieżka do pliku wyjściowego CSV z wynikami analizy
    output_svg = 'data/word_frequency.svg'  # Ścieżka do pliku wyjściowego SVG z wykresem częstotliwości słów

    analyzer = TextAnalyzer(input_file)  # Tworzymy instancję klasy TextAnalyzer, przekazując ścieżkę do pliku wejściowego
    analyzer.save_results(output_csv)  # Zapisujemy wyniki analizy do pliku CSV

    word_freq = analyzer.most_common_words()  # Pobieramy najczęściej występujące słowa

    # Pobieramy najczęściej występujące słowo i jego częstotliwość
    most_common_word, frequency = word_freq[0]
    # Drukujemy najczęściej używane słowo w kolorze czerwonym
    print(f"{Fore.RED}Najczęściej używane słowo: {most_common_word}")
    # Drukujemy liczbę wystąpień tego słowa w kolorze niebieskim
    print(f"{Fore.BLUE}Ilość wystąpień: {frequency}")

    plotter = Plotter(word_freq)  # Tworzymy instancję klasy Plotter, przekazując listę częstotliwości słów
    plotter.plot_word_frequency(output_svg)  # Tworzymy wykres częstotliwości słów i zapisujemy go do pliku SVG

# Uruchamiamy funkcję main, jeśli skrypt jest wykonywany bezpośrednio
if __name__ == "__main__":
    main()
