# Author: Kaustav Ghosh
# Problem: Can Make Arithmetic Progression From Sequence
# Approach: The elements can be rearranged freely, and the only possible arithmetic order is the sorted one, so sort and check that every consecutive gap matches the first

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ordered = sorted(arr)
        step = ordered[1] - ordered[0]
        return all(b - a == step for a, b in zip(ordered, ordered[1:]))
