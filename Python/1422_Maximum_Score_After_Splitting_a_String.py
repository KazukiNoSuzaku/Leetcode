# Author: Kaustav Ghosh
# Problem: Maximum Score After Splitting a String
# Approach: For each split point count zeros on left plus ones on right

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')
        zeros = 0
        best = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            best = max(best, zeros + ones)
        return best
