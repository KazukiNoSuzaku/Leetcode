# Author: Kaustav Ghosh
# Problem: Minimum Elements to Add to Form a Given Sum
# Approach: Each added element can shift the sum by at most `limit`, so the answer is ceil(|goal - current sum| / limit)

class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        gap = abs(goal - sum(nums))
        return (gap + limit - 1) // limit
