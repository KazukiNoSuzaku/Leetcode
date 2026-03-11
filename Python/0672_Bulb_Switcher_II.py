# Count distinct states of n bulbs after m operations from 4 switch types.

# Author: Kaustav Ghosh

class Solution(object):
    def flipLights(self, n, presses):
        if presses == 0: return 1
        n = min(n, 3)
        if n == 1: return 2
        if n == 2: return 3 if presses == 1 else 4
        if presses == 1: return 4
        if presses == 2: return 7
        return 8
