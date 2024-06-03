import csv
from collections import Counter

class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.text = self._load_text()

    def _load_text(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()

    def word_count(self):
        words = self.text.split()
        return len(words)

    def most_common_words(self, n=10):
        words = self.text.split()
        word_freq = Counter(words)
        return word_freq.most_common(n)

    def save_results(self, output_file):
        word_freq = self.most_common_words()
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Word', 'Frequency'])
            for word, freq in word_freq:
                writer.writerow([word, freq])
