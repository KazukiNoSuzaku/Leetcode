# Author: Kaustav Ghosh
# Problem: Replace Non-Coprime Numbers in Array
# Approach: Use a stack. Push each number, but while it shares a common factor with the top of the stack, pop the top and merge them into their LCM. A merge can create a new common factor with the new top, so keep merging until coprime, then push

from math import gcd


class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        for x in nums:
            while stack:
                g = gcd(stack[-1], x)
                if g == 1:
                    break
                x = stack.pop() // g * x  # lcm(top, x)
            stack.append(x)
        return stack
