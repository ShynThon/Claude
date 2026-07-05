def count_words(text):
    return len(text.split())


def average_word_length(text):
    words = text.split()
    if not words:
        return 0.0
    return sum(len(word) for word in words) / len(words)


def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)
