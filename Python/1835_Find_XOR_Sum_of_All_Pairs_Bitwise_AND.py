# Author: Kaustav Ghosh
# Problem: Find XOR Sum of All Pairs Bitwise AND
# Approach: Looking at one bit at a time, that bit is set in the answer when an odd number of pairs have it set in both operands, and the number of such pairs is the count of values carrying the bit in the first array multiplied by the count in the second. A product is odd exactly when both factors are, so the bit survives precisely when it survives the XOR of each array separately. That holds for every bit independently, so the whole answer is the XOR of one array ANDed with the XOR of the other, which costs one pass over each instead of visiting all ten billion pairs.

class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        first = 0
        for value in arr1:
            first ^= value
        second = 0
        for value in arr2:
            second ^= value
        return first & second
