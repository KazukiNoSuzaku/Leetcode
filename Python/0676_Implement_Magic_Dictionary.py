# Design a magic dictionary that checks if a word can match any stored word with exactly 1 change.

# Author: Kaustav Ghosh

class MagicDictionary(object):
    def __init__(self):
        self.words = []

    def buildDict(self, dictionary):
        self.words = dictionary

    def search(self, searchWord):
        for word in self.words:
            if len(word) == len(searchWord) and sum(a != b for a, b in zip(word, searchWord)) == 1:
                return True
        return False
