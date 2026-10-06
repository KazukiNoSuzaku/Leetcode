# Author: Kaustav Ghosh
# Problem: Shuffle String
# Approach: indices is a permutation telling each character where it belongs, so write every character straight into its destination slot and join the result

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffled = [''] * len(s)
        for ch, position in zip(s, indices):
            shuffled[position] = ch
        return "".join(shuffled)
