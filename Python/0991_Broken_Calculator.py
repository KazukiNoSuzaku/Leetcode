# On a broken calculator, you can double or decrement the display.
# Return minimum operations to reach target from startValue.

# Author: Kaustav Ghosh

class Solution(object):
    def brokenCalc(self, startValue, target):
        ops = 0
        while target > startValue:
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
            ops += 1
        return ops + startValue - target
