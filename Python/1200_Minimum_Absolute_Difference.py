# Author: Kaustav Ghosh
# Sort array, find minimum adjacent difference, collect all pairs with that difference

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
        return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == min_diff]
