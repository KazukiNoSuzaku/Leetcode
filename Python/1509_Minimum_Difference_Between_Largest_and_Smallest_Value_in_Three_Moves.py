# Author: Kaustav Ghosh
# Problem: Minimum Difference Between Largest and Smallest Value in Three Moves
# Approach: Changing a value freely is as good as discarding it, and only extremes are ever worth discarding, so after sorting the three removals split between the two ends. That leaves four candidate windows, and the smallest spread among them wins; four or fewer elements collapse to zero

class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        ordered = sorted(nums)
        return min(ordered[len(ordered) - 4 + i] - ordered[i] for i in range(4))
