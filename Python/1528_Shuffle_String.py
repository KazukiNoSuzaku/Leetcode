# Author: Kaustav Ghosh
# Problem: 1528 - Shuffle String
# Approach: Place each character at indices[i]

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result = [''] * len(s)
        for i, idx in enumerate(indices):
            result[idx] = s[i]
        return ''.join(result)
