# Author: Kaustav Ghosh
# Problem: Minimum Addition to Make Integer Beautiful
# Approach: Lowering a digit sum means carrying, so round n up to the next multiple of 10, then of 100, and so on, which zeroes the trailing digits one more at a time. The first rounding whose digit sum fits the target is the cheapest, since any smaller addition leaves those digits non-zero

class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        def digit_sum(x):
            return sum(int(d) for d in str(x))

        rounded = n
        power = 10
        while digit_sum(rounded) > target:
            rounded = (n // power + 1) * power
            power *= 10
        return rounded - n
