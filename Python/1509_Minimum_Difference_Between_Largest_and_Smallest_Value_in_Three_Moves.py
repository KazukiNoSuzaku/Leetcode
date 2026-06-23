# Author: Kaustav Ghosh
# Problem: Minimum Difference Between Largest and Smallest Value in Three Moves
# Approach: Sort, try all 4 ways to remove 3 elements from the ends

class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        return min(
            nums[n - 1] - nums[3],
            nums[n - 2] - nums[2],
            nums[n - 3] - nums[1],
            nums[n - 4] - nums[0]
        )
