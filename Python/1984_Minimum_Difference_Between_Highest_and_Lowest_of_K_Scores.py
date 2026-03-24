# Author: Kaustav Ghosh
# Problem 1984: Minimum Difference Between Highest and Lowest of K Scores

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
