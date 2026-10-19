# Author: Kaustav Ghosh
# Problem: Check Array Formation Through Concatenation
# Approach: The pieces may be reordered but never reversed or split, and all the integers are distinct, so each value belongs to exactly one piece and the first value of a piece determines the whole piece uniquely. Walking the target array and looking up the piece starting at the current value therefore leaves no choice at any step: either that piece continues to match the array exactly, or the arrangement is impossible.

class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        starts = {piece[0]: piece for piece in pieces}
        i = 0
        n = len(arr)
        while i < n:
            piece = starts.get(arr[i])
            if piece is None:
                return False
            for value in piece:
                if i >= n or arr[i] != value:
                    return False
                i += 1
        return True
