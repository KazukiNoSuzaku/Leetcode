# Author: Kaustav Ghosh
# Problem: Maximum Element After Decreasing and Rearranging
# Approach: Sort, force the first element to 1, then each element can be at most previous+1; the last value is the achievable maximum

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        prev = 0
        for x in arr:
            prev = min(prev + 1, x)
        return prev
