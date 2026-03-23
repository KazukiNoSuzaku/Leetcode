# Author: Kaustav Ghosh
# Problem 1835: Find XOR Sum of All Pairs Bitwise AND

class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        xor1 = 0
        for x in arr1:
            xor1 ^= x
        xor2 = 0
        for x in arr2:
            xor2 ^= x
        return xor1 & xor2
