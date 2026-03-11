# Determine if two sentences are similar given pairs of similar words (non-transitive).

# Author: Kaustav Ghosh

class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2): return False
        pairs = set(map(tuple, similarPairs))
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and (w1, w2) not in pairs and (w2, w1) not in pairs:
                return False
        return True
