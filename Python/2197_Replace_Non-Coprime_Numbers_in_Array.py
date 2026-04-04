# Author: Kaustav Ghosh

from math import gcd

class Solution(object):
    def replaceNonCoprimes(self, nums):
        # type: (List[int]) -> List[int]
        stack = []
        for x in nums:
            stack.append(x)
            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                b = stack.pop()
                a = stack.pop()
                lcm = a * b // gcd(a, b)
                stack.append(lcm)
        return stack
