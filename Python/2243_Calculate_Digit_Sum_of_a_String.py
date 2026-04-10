# Author: Kaustav Ghosh
# Problem: 2243. Calculate Digit Sum of a String
# URL: https://leetcode.com/problems/calculate-digit-sum-of-a-string/
# Difficulty: Easy
#
# Approach:
# Repeatedly split the string into groups of size k, replace each group
# with its digit sum, and concatenate until the length is at most k.

class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                group = s[i:i + k]
                total = sum(int(c) for c in group)
                new_s += str(total)
            s = new_s
        return s
