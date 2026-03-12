# Author: Kaustav Ghosh
# 1122. Relative Sort Array
# https://leetcode.com/problems/relative-sort-array/

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        order = {v: i for i, v in enumerate(arr2)}
        n = len(arr2)
        return sorted(arr1, key=lambda x: (order[x], x) if x in order else (n, x))
