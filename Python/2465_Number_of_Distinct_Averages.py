# Author: Kaustav Ghosh
# Problem: Number of Distinct Averages
# Approach: Sorting pairs the smallest remaining element with the largest, so the pairs are simply the ends working inward. Two averages are equal exactly when their sums are, so count the distinct pair sums

class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ordered = sorted(nums)
        return len({ordered[i] + ordered[len(ordered) - 1 - i] for i in range(len(ordered) // 2)})
