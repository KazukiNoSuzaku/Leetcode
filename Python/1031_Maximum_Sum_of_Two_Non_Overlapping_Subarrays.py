# Author: Kaustav Ghosh
# 1031. Maximum Sum of Two Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def window_sum(l, r):
            return prefix[r] - prefix[l]

        def helper(L, M):
            # max sum of L-length window before each position + M-length window after
            res = 0
            max_l = 0
            for i in range(L + M, n + 1):
                max_l = max(max_l, window_sum(i - L - M, i - M))
                res = max(res, max_l + window_sum(i - M, i))
            return res

        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))
