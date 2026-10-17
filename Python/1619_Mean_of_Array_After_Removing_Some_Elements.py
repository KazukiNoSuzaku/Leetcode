# Author: Kaustav Ghosh
# Problem: Mean of Array After Removing Some Elements
# Approach: Removing the smallest five percent and the largest five percent is, once the values are sorted, just discarding a fixed-size block from each end, and the length is guaranteed to be a multiple of twenty so the five percent is always a whole number of elements. The mean of what is left is then taken over that middle slice directly.

class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        ordered = sorted(arr)
        cut = len(ordered) // 20
        middle = ordered[cut:len(ordered) - cut]
        return float(sum(middle)) / len(middle)
