# Author: Kaustav Ghosh
# Problem: Largest Substring Between Two Equal Characters
# Approach: For any character the widest gap is always between its first and its last appearance, so there is no need to consider intermediate pairs: one pass recording where each character was first seen lets every later appearance be measured against that first position immediately. The answer counts the characters strictly between the two ends, which is the index difference minus one, and a character seen only once contributes nothing.

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_seen = {}
        best = -1
        for i, ch in enumerate(s):
            if ch in first_seen:
                if i - first_seen[ch] - 1 > best:
                    best = i - first_seen[ch] - 1
            else:
                first_seen[ch] = i
        return best
