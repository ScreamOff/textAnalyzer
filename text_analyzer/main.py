from analyzer import TextAnalyzer
from plotter import Plotter
from colorama import Fore, init

def main():
    init(autoreset=True)

    input_file = 'data/input.txt'
    output_csv = 'data/output.csv'
    output_svg = 'data/word_frequency.svg'

    analyzer = TextAnalyzer(input_file)
    analyzer.save_results(output_csv)

    word_freq = analyzer.most_common_words()

    most_common_word, frequency = word_freq[0]
    print(f"{Fore.RED}Najczęściej używane słowo: {most_common_word}")
    print(f"{Fore.BLUE}Ilość wystąpień: {frequency}")

    plotter = Plotter(word_freq)
    plotter.plot_word_frequency(output_svg)

if __name__ == "__main__":
    main()
