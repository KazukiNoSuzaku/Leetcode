# Author: Kaustav Ghosh
# Problem: Number of Excellent Pairs
# Approach: For any pair, popcount(a | b) + popcount(a & b) equals popcount(a) + popcount(b), since every bit is counted once by the OR and again by the AND only when both have it. So only popcounts of the distinct values matter: bucket them by popcount and, for each bucket, add the number of values whose popcount is at least k minus this one

class Solution(object):
    def countExcellentPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        bits = [0] * 32
        for x in set(nums):
            bits[bin(x).count('1')] += 1
        at_least = [0] * 33
        for b in range(31, -1, -1):
            at_least[b] = at_least[b + 1] + bits[b]
        total = 0
        for b in range(32):
            if bits[b]:
                need = min(max(k - b, 0), 32)
                total += bits[b] * at_least[need]
        return total
