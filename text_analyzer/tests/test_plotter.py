import sys
import os
import unittest
from plotter import Plotter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestPlotter(unittest.TestCase):
    def test_plot_creation(self):
        data = [('Maciek', 200), ('Daniel', 100)]
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        plotter = Plotter(data)
        plotter.plot_word_frequency(os.path.join(base_path, 'data', 'test_word_frequency.svg'))

if __name__ == '__main__':
    unittest.main()
