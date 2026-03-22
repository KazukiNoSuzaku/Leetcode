# Author: Kaustav Ghosh

class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        # words1 is shorter
        n1, n2 = len(words1), len(words2)
        left = 0
        while left < n1 and words1[left] == words2[left]:
            left += 1
        right = 0
        while right < n1 - left and words1[n1 - 1 - right] == words2[n2 - 1 - right]:
            right += 1
        return left + right >= n1
