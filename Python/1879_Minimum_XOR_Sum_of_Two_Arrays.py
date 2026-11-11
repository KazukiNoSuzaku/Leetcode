# Author: Kaustav Ghosh
# Problem: Minimum XOR Sum of Two Arrays
# Approach: The order of the first array is fixed, so after choosing partners for its first few entries the only thing that matters is which entries of the second array have been used, not which went where. That makes the state a bitmask over at most fourteen positions, and how many bits are set says which entry of the first array is being matched next, so no separate index has to be stored. Each state then tries every unused partner, which visits each of the sixteen thousand masks with fourteen transitions instead of enumerating all the orderings.

class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        full = 1 << n
        INF = float("inf")
        best = [INF] * full
        best[0] = 0
        for mask in range(full):
            if best[mask] == INF:
                continue
            position = bin(mask).count("1")
            if position == n:
                continue
            value = nums1[position]
            for other in range(n):
                if mask >> other & 1:
                    continue
                cost = best[mask] + (value ^ nums2[other])
                nxt = mask | 1 << other
                if cost < best[nxt]:
                    best[nxt] = cost
        return best[full - 1]
