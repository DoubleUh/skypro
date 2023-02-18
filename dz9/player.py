class Player:

    def __init__(self, name):
        self.name = name
        self.user_subwords = []

    def count_used_words(self):
        return len(self.user_subwords)

    def add_word_in_subwords(self, word):
        """Добавляет слово"""
        self.user_subwords.append(word)

    def is_word_in_user_subwords(self, word):
        return word in self.user_subwords

    def __repr__(self):
        return f"{self.name} - {self.user_subwords}"