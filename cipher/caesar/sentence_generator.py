import random


class SentenceGenerator:
    with open("../words.txt") as f:
        words = [w.rstrip().lower() for w in f.readlines()]

    @classmethod
    def generate(cls):
        selected_words = random.sample(cls.words, 10)
        return " ".join(selected_words)
