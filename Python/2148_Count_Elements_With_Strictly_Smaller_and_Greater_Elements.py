# Author: Kaustav Ghosh
# Problem: Count Elements With Strictly Smaller and Greater Elements
# Approach: An element qualifies iff it is neither the minimum nor the maximum of the array; count values strictly between them

class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = min(nums), max(nums)
        return sum(1 for v in nums if lo < v < hi)
