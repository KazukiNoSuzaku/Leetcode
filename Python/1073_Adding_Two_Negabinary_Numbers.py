# Author: Kaustav Ghosh
# 1073. Adding Two Negabinary Numbers
# https://leetcode.com/problems/adding-two-negabinary-numbers/

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            val = carry
            if i >= 0:
                val += arr1[i]
                i -= 1
            if j >= 0:
                val += arr2[j]
                j -= 1
            # In base -2: digit is val % 2, carry is -(val // 2)
            result.append(val & 1)
            carry = -(val >> 1)
        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]
