# Author: Kaustav Ghosh
# Problem: Maximize Score After N Operations
# Approach: Only which numbers have already been consumed matters, not how they were grouped, so the state is a bitmask over the at most fourteen values and the operation number falls out of how many bits are set. The order in which pairs are taken genuinely matters here, because the multiplier grows with each operation and a large divisor is worth more later, so every free pair has to be considered at every state rather than only the pairs containing the first unused value. The pairwise divisors are computed once up front since each pair is consulted from many different masks.

class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from math import gcd

        m = len(nums)
        divisor = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                divisor[i][j] = gcd(nums[i], nums[j])

        full = 1 << m
        best = [-1] * full
        best[0] = 0
        for mask in range(full):
            if best[mask] < 0:
                continue
            used = bin(mask).count("1")
            if used == m:
                continue
            operation = used // 2 + 1
            for i in range(m):
                if mask >> i & 1:
                    continue
                for j in range(i + 1, m):
                    if mask >> j & 1:
                        continue
                    nxt = mask | 1 << i | 1 << j
                    score = best[mask] + operation * divisor[i][j]
                    if score > best[nxt]:
                        best[nxt] = score
        return best[full - 1]
