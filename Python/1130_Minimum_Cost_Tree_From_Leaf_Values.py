# Author: Kaustav Ghosh
# 1130. Minimum Cost Tree From Leaf Values
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float('inf')]
        result = 0
        for val in arr:
            while stack[-1] <= val:
                mid = stack.pop()
                result += mid * min(stack[-1], val)
            stack.append(val)
        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        return result
