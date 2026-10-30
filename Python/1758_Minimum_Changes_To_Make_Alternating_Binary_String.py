# Author: Kaustav Ghosh
# Problem: Minimum Changes To Make Alternating Binary String
# Approach: There are only two alternating strings of a given length, the one starting with zero and the one starting with one, and they disagree at every position, so a character matching one of them necessarily mismatches the other. Counting the mismatches against the zero-first pattern therefore gives the other count for free as the length minus it, and the answer is the smaller of the two; one pass over the string suffices.

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        wrong = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                wrong += 1
        return min(wrong, len(s) - wrong)
