# Author: Kaustav Ghosh

class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        perm = list(range(n))
        target = list(range(n))
        ops = 0
        while True:
            ops += 1
            new_perm = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    new_perm[i] = perm[i // 2]
                else:
                    new_perm[i] = perm[n // 2 + (i - 1) // 2]
            perm = new_perm
            if perm == target:
                return ops
