# Find minimum steps to reach target on number line (step i goes left or right i).

# Author: Kaustav Ghosh

class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        step = total = 0
        while total < target or (total - target) % 2 != 0:
            step += 1
            total += step
        return step
