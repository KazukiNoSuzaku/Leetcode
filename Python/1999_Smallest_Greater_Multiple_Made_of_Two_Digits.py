# Author: Kaustav Ghosh
# Problem: Smallest Greater Multiple Made of Two Digits
# Approach: Walking multiples of the divisor would mean testing far too many numbers, so the search runs over the numbers built from the two allowed digits instead, of which there are at most about a thousand inside the signed 32-bit range. Generating them breadth first, shortest first and with the smaller digit appended before the larger one, makes them come out in increasing numeric order, so the first candidate that exceeds the divisor and divides evenly by it is the answer. Two digits of zero can only ever build zero, and running past the 32-bit limit means nothing qualifies.

class Solution(object):
    def findInteger(self, k, digit1, digit2):
        """
        :type k: int
        :type digit1: int
        :type digit2: int
        :rtype: int
        """
        LIMIT = 2 ** 31 - 1
        small, large = sorted((digit1, digit2))
        if large == 0:
            return -1
        digits = [small, large] if small != large else [small]

        frontier = [digit for digit in digits if digit != 0]
        while frontier:
            following = []
            for value in frontier:
                if value > LIMIT:
                    return -1
                if value > k and value % k == 0:
                    return value
                for digit in digits:
                    following.append(value * 10 + digit)
            frontier = following
        return -1
