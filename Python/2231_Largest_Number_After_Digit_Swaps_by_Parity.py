# Author: Kaustav Ghosh
# Problem: Largest Number After Digit Swaps by Parity
# Approach: Swaps are only allowed between digits of the same parity, so each parity class can be arranged independently. Sort the odd digits and the even digits each in descending order, then place them back into their original parity positions to maximize the number

class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(c) for c in str(num)]
        odds = sorted((d for d in digits if d % 2 == 1), reverse=True)
        evens = sorted((d for d in digits if d % 2 == 0), reverse=True)
        oi = ei = 0
        result = []
        for d in digits:
            if d % 2 == 1:
                result.append(odds[oi]); oi += 1
            else:
                result.append(evens[ei]); ei += 1
        return int("".join(map(str, result)))
