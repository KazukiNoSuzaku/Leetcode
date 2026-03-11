# Replace all words in a sentence with their shortest root from a dictionary.

# Author: Kaustav Ghosh

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        root_set = set(dictionary)
        def replace(word):
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]
            return word
        return ' '.join(replace(w) for w in sentence.split())
