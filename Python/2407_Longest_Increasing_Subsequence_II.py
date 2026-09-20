# Author: Kaustav Ghosh
# Problem: Longest Increasing Subsequence II
# Approach: The subsequence ending at value x can extend any subsequence whose last value lies in [x - k, x - 1], so index the best length by value rather than by position. An iterative segment tree over the value range answers that range maximum and records the new length in logarithmic time per element

class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = max(nums) + 1
        tree = [0] * (2 * size)

        def range_max(lo, hi):
            result = 0
            lo += size
            hi += size
            while lo < hi:
                if lo & 1:
                    result = max(result, tree[lo])
                    lo += 1
                if hi & 1:
                    hi -= 1
                    result = max(result, tree[hi])
                lo >>= 1
                hi >>= 1
            return result

        def put(value, length):
            i = value + size
            if tree[i] >= length:
                return
            tree[i] = length
            i >>= 1
            while i:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i >>= 1

        best = 0
        for x in nums:
            length = range_max(max(0, x - k), x) + 1
            put(x, length)
            best = max(best, length)
        return best
