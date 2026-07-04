# Author: Kaustav Ghosh
# Problem: Mean of Array After Removing Some Elements
# Approach: Sort, drop the smallest 5% and largest 5% (n/20 each), and average the trimmed middle

class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        n = len(arr)
        cut = n // 20
        trimmed = arr[cut:n - cut]
        return sum(trimmed) / float(len(trimmed))
