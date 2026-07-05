# Claude

A tiny Python utility for basic word statistics on a piece of text.

## Usage

```python
from word_stats import average_word_length, count_words, longest_word

text = "the quick brown fox"
count_words(text)          # 4
average_word_length(text)  # 4.0
longest_word(text)         # "quick"
```

## Running tests

```bash
python -m unittest
```
