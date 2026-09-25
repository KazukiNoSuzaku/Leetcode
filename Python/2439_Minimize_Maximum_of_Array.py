# Author: Kaustav Ghosh
# Problem: Minimize Maximum of Array
# Approach: A value can only ever be pushed to the left, so any prefix keeps its total and its largest element can be no smaller than that total averaged over the prefix, rounded up. That bound is reachable everywhere at once, so the answer is the largest such prefix average

class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0
        total = 0
        for i, x in enumerate(nums):
            total += x
            best = max(best, -(-total // (i + 1)))
        return best
