# Author: Kaustav Ghosh
# Problem: Minimum Elements to Add to Form a Given Sum
# Approach: Only the shortfall between the current sum and the goal matters, and every element added may contribute at most limit towards closing it, in whichever direction is needed. Spending the full limit on each addition is therefore always optimal, so the count is the shortfall divided by limit rounded up, computed with integer arithmetic to stay exact at the billion-scale goals the constraints allow.

class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        shortfall = abs(goal - sum(nums))
        return -(-shortfall // limit)
