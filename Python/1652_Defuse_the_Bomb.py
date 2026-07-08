# Author: Kaustav Ghosh
# Problem: Defuse the Bomb
# Approach: For each index sum the k neighbors forward (k>0) or backward (k<0) on the circular array; k==0 yields all zeros

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        offsets = range(1, k + 1) if k > 0 else range(k, 0)
        for i in range(n):
            res[i] = sum(code[(i + j) % n] for j in offsets)
        return res
