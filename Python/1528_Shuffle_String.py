# Author: Kaustav Ghosh
# Problem: Shuffle String
# Approach: Place each character at its target index directly into result array

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
