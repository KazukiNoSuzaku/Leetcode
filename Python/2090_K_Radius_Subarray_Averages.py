# Author: Kaustav Ghosh
# Problem 2090: K Radius Subarray Averages

class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1] * n
        if 2 * k + 1 > n:
            return result
        window_sum = sum(nums[:2 * k + 1])
        window_size = 2 * k + 1
        result[k] = window_sum // window_size
        for i in range(k + 1, n - k):
            window_sum += nums[i + k] - nums[i - k - 1]
            result[i] = window_sum // window_size
        return result
