class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def is_subwords(self, word):
        return word in self.subwords

    def count_subwords(self):
        return len(self.subwords)

    def __repr__(self):
        return f"Слово {self.word} - {self.subwords}"