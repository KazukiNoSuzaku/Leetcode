# Author: Kaustav Ghosh
# https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        mapping = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in mapping:
                return False
            piece = mapping[arr[i]]
            for val in piece:
                if i >= len(arr) or arr[i] != val:
                    return False
                i += 1
        return True
