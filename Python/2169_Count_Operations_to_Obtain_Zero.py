# Author: Kaustav Ghosh
# Problem: 2169. Count Operations to Obtain Zero
# URL: https://leetcode.com/problems/count-operations-to-obtain-zero/
# Difficulty: Easy

class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        ops = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                ops += num1 // num2
                num1 %= num2
            else:
                ops += num2 // num1
                num2 %= num1
        return ops
