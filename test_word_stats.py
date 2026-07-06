import unittest

from word_stats import average_word_length, count_words, longest_word


class WordStatsTests(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("the quick brown fox"), 4)

    def test_average_word_length(self):
        self.assertAlmostEqual(average_word_length("cat dog"), 3.0)

    def test_longest_word(self):
        self.assertEqual(longest_word("cat elephant dog"), "elephant")

    def test_count_words_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_average_word_length_empty_string(self):
        self.assertEqual(average_word_length(""), 0.0)

    def test_longest_word_empty_string(self):
        self.assertEqual(longest_word(""), "")


if __name__ == "__main__":
    unittest.main()
