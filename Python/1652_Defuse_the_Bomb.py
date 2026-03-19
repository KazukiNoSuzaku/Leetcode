# Author: Kaustav Ghosh
# https://leetcode.com/problems/defuse-the-bomb/

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        result = [0] * n
        if k == 0:
            return result
        for i in range(n):
            if k > 0:
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            else:
                result[i] = sum(code[(i + j) % n] for j in range(k, 0))
        return result
