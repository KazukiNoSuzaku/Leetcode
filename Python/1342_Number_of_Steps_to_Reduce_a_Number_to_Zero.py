# If even, divide by 2. If odd, subtract 1. Return steps to reach 0.

# Author: Kaustav Ghosh

class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while num:
            steps += 1 if num % 2 == 0 else 2
            num >>= 1
        return steps - (1 if steps > 0 else 0)
