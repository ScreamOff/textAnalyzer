import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, data):
        self.data = data

    def plot_word_frequency(self, output_file):
        words, frequencies = zip(*self.data)
        plt.figure(figsize=(10, 8))
        plt.bar(words, frequencies, color='blue')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title('Top Word Frequencies')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_file)
