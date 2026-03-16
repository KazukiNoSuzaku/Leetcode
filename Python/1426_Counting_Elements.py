# Author: Kaustav Ghosh
# Problem: Counting Elements (Premium)
# Approach: Check if x+1 exists in set for each element

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = set(arr)
        return sum(1 for x in arr if x + 1 in s)
