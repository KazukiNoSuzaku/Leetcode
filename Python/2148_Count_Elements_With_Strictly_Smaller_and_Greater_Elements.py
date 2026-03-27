# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)
        return sum(1 for x in nums if min_val < x < max_val)
