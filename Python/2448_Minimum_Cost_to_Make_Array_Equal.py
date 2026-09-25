# Author: Kaustav Ghosh
# Problem: Minimum Cost to Make Array Equal
# Approach: The total cost as a function of the chosen target is piecewise linear and bends only at the array's own values, so the cheapest target is the weighted median: sort by value and walk until the accumulated cost reaches half the total. Summing the weighted distances to that value gives the answer

class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        pairs = sorted(zip(nums, cost))
        half = sum(cost)
        accumulated = 0
        target = pairs[0][0]
        for value, weight in pairs:
            accumulated += weight
            if accumulated * 2 >= half:
                target = value
                break
        return sum(abs(value - target) * weight for value, weight in pairs)
