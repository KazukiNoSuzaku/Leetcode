# Author: Kaustav Ghosh
# Problem: Find XOR Sum of All Pairs Bitwise AND
# Approach: XOR over all (a AND b) distributes: sum = (XOR of arr1) AND (XOR of arr2), since each product term factors out over the two arrays

from functools import reduce
from operator import xor

class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        return reduce(xor, arr1) & reduce(xor, arr2)
