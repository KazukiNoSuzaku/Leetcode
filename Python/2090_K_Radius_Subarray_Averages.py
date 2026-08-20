# Author: Kaustav Ghosh
# Problem: K Radius Subarray Averages
# Approach: Use prefix sums to get each radius-k window sum in O(1). Positions without a full window on both sides are -1; otherwise the average is the floor of the window sum over 2k+1

class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        window = 2 * k + 1
        result = [-1] * n
        if window > n:
            return result
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v
        for i in range(k, n - k):
            total = prefix[i + k + 1] - prefix[i - k]
            result[i] = total // window
        return result
