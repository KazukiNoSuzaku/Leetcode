# Author: Kaustav Ghosh
# Problem: 2279. Maximum Bags With Full Capacity of Rocks
# URL: https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
# Difficulty: Medium
#
# Approach:
# Compute remaining capacity for each bag, sort ascending, greedily fill
# bags starting from those needing the fewest rocks.

class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        remaining = sorted(c - r for c, r in zip(capacity, rocks))
        count = 0
        for need in remaining:
            if additionalRocks >= need:
                additionalRocks -= need
                count += 1
            else:
                break
        return count
