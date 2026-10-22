# Author: Kaustav Ghosh
# Problem: Maximum Repeating Substring
# Approach: The repetitions have to be consecutive, so the question is simply the largest k for which the word repeated k times appears as a substring, and that condition is monotone: if k copies fit then so do k-1. So I raise k from one upward and stop at the first failure, which is the answer plus one. The number of iterations is bounded by the sequence length divided by the word length, and each test is a single substring search.

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 0
        while word * (count + 1) in sequence:
            count += 1
        return count
