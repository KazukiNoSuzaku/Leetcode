# Author: Kaustav Ghosh
# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ['a'] * n
        k -= n  # each position starts as 'a' (value 1)
        i = n - 1
        while k > 0:
            add = min(25, k)
            result[i] = chr(ord('a') + add)
            k -= add
            i -= 1
        return ''.join(result)
