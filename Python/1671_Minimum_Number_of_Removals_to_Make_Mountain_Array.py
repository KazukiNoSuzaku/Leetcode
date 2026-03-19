# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        n = len(nums)

        # LIS ending at i
        lis = [0] * n
        dp = []
        for i in range(n):
            pos = bisect.bisect_left(dp, nums[i])
            if pos == len(dp):
                dp.append(nums[i])
            else:
                dp[pos] = nums[i]
            lis[i] = pos + 1

        # LDS starting at i (LIS from right)
        lds = [0] * n
        dp = []
        for i in range(n - 1, -1, -1):
            pos = bisect.bisect_left(dp, nums[i])
            if pos == len(dp):
                dp.append(nums[i])
            else:
                dp[pos] = nums[i]
            lds[i] = pos + 1

        max_mountain = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                max_mountain = max(max_mountain, lis[i] + lds[i] - 1)
        return n - max_mountain
