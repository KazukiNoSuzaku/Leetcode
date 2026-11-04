# Author: Kaustav Ghosh
# Problem: Sentence Similarity III
# Approach: Inserting a block of words into one sentence to produce the other means the two sentences agree on some prefix of words and some suffix of words, with the whole difference sitting between them. So the matching words are peeled off both ends simultaneously, and the sentences are similar exactly when one of them runs out, which is the case where everything left over in the longer sentence is the inserted block. Comparing whole words rather than characters is what keeps a word being cut in half from counting as a match.

class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        first = sentence1.split()
        second = sentence2.split()
        if len(first) > len(second):
            first, second = second, first

        start = 0
        while start < len(first) and first[start] == second[start]:
            start += 1
        end = 0
        while end < len(first) - start and first[-1 - end] == second[-1 - end]:
            end += 1
        return start + end == len(first)
