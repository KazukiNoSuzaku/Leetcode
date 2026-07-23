# Author: Kaustav Ghosh
# Problem: Sentence Similarity III
# Approach: One sentence must be the other with a block inserted in the middle, so the shorter's words must all be covered by a shared prefix plus a shared suffix

class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        w1 = sentence1.split()
        w2 = sentence2.split()
        if len(w1) > len(w2):
            w1, w2 = w2, w1  # w1 is the shorter one

        i = 0
        while i < len(w1) and w1[i] == w2[i]:
            i += 1

        j = 0
        while j < len(w1) - i and w1[-1 - j] == w2[-1 - j]:
            j += 1

        return i + j >= len(w1)
