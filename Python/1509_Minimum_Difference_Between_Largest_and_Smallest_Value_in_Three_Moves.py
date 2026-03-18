# In at most 3 moves you can change any element to any value.
# Return the minimum difference between max and min after 3 moves.

# Author: Kaustav Ghosh

class Solution(object):
    def minDifference(self, nums):
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        # Remove 3 elements from either end in 4 combinations
        return min(
            nums[n-1] - nums[3],
            nums[n-2] - nums[2],
            nums[n-3] - nums[1],
            nums[n-4] - nums[0]
        )
