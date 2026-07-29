# Author: Kaustav Ghosh
# Problem: Minimize Maximum Pair Sum in Array
# Approach: Sort and pair each smallest element with the corresponding largest; the maximum such pair sum is minimized

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        return max(nums[i] + nums[n - 1 - i] for i in range(n // 2))
