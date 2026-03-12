# Author: Kaustav Ghosh
# Gray code starting from given start value using XOR

class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        result = []
        for i in range(1 << n):
            result.append(start ^ i ^ (i >> 1))
        return result
