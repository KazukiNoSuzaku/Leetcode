# Author: Kaustav Ghosh
# Problem: Count Ways to Distribute Candies
# Approach: The bags are indistinguishable and must all be non-empty, so this counts partitions of a labelled set into a fixed number of unlabelled blocks, which is a Stirling number of the second kind. Rather than any formula with alternating signs, it is built up by deciding where the newest candy goes: either it opens a fresh bag, which leaves the earlier candies filling one bag fewer, or it joins one of the bags already open, which can happen in as many ways as there are such bags. Each row of the table depends only on the row before it, so one array updated from the high end downwards is enough.

class Solution(object):
    def waysToDistribute(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        ways = [0] * (k + 1)
        ways[0] = 1
        for candy in range(1, n + 1):
            top = k if k < candy else candy
            for bags in range(top, 0, -1):
                ways[bags] = (ways[bags - 1] + ways[bags] * bags) % MOD
            ways[0] = 0
        return ways[k]
