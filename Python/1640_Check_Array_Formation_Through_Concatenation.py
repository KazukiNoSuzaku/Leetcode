# Author: Kaustav Ghosh
# Problem: Check Array Formation Through Concatenation
# Approach: Values are distinct, so index each piece by its first element; walk arr, and at each step the current value must start a piece that then matches exactly

class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        start = {piece[0]: piece for piece in pieces}
        i, n = 0, len(arr)
        while i < n:
            if arr[i] not in start:
                return False
            for value in start[arr[i]]:
                if i >= n or arr[i] != value:
                    return False
                i += 1
        return True
