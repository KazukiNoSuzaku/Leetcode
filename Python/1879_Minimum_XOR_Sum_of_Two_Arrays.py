# Author: Kaustav Ghosh
# Problem 1879: Minimum XOR Sum of Two Arrays

class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            i = bin(mask).count('1')
            if i >= n:
                continue
            for j in range(n):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + (nums1[i] ^ nums2[j]))
        return dp[(1 << n) - 1]
