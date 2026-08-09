# Author: Kaustav Ghosh
# Problem: Binary Searchable Numbers in an Unsorted Array
# Approach: A value is guaranteed findable by binary search regardless of the comparator's guidance exactly when it is larger than everything to its left and smaller than everything to its right. Sweep prefix maxima and suffix minima to count such pivots

class Solution(object):
    def binarySearchableNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_max = [float('-inf')] * n
        suffix_min = [float('inf')] * n
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i - 1])
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i + 1])
        return sum(1 for i in range(n)
                   if prefix_max[i] < nums[i] < suffix_min[i])
