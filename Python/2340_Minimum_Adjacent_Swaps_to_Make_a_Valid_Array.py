# Author: Kaustav Ghosh
# Problem: Minimum Adjacent Swaps to Make a Valid Array
# Approach: Bubble the leftmost minimum to index 0 (costs its index) and the rightmost maximum to the end (costs n - 1 - its index). If the minimum starts to the right of the maximum, their paths cross and one swap advances both, so subtract one

class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lo = hi = 0
        for i, x in enumerate(nums):
            if x < nums[lo]:
                lo = i
            if x >= nums[hi]:
                hi = i
        swaps = lo + (n - 1 - hi)
        return swaps - 1 if lo > hi else swaps
