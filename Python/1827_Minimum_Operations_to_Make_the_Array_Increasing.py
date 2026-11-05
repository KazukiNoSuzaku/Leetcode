# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make the Array Increasing
# Approach: Values can only be raised, so each element has to end up at least one above whatever its predecessor settled on, and raising it any further than that would only make the elements after it more expensive. Keeping the smallest legal value for each position is therefore optimal, and the cost of a position is the gap between that value and what it already held.

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        previous = 0
        for value in nums:
            if value <= previous:
                operations += previous + 1 - value
                previous = previous + 1
            else:
                previous = value
        return operations
