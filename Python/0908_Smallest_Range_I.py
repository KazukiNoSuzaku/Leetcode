# Find minimum possible score after adding k in [-k,k] to each element.

# Author: Kaustav Ghosh

class Solution(object):
    def smallestRangeI(self, nums, k):
        return max(0, max(nums) - min(nums) - 2 * k)
