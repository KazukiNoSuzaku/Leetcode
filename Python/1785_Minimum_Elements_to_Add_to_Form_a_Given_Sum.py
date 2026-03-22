# Author: Kaustav Ghosh

class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        diff = abs(goal - sum(nums))
        return (diff + limit - 1) // limit
