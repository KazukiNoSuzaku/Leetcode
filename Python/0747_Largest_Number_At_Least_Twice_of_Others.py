# Check if the largest element is at least twice as large as every other element.

# Author: Kaustav Ghosh

class Solution(object):
    def dominantIndex(self, nums):
        m = max(nums)
        idx = nums.index(m)
        if all(m >= 2 * x for x in nums if x != m):
            return idx
        return -1
