# Return any array of n unique integers that sum to zero.

# Author: Kaustav Ghosh

class Solution(object):
    def sumZero(self, n):
        res = list(range(1, n))
        res.append(-sum(res))
        return res
