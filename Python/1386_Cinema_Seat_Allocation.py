# Author: Kaustav Ghosh
# Problem: Cinema Seat Allocation
# Approach: Bitmask per row tracking reserved seats, check groups of 4

from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved = defaultdict(int)
        for row, seat in reservedSeats:
            reserved[row] |= 1 << seat

        result = 2 * n  # max 2 groups per row
        for row, mask in reserved.items():
            left = not (mask & 0b0000111100)   # seats 2-5
            middle = not (mask & 0b0001111000)  # seats 4-7
            right = not (mask & 0b0111100000)   # seats 6-9
            if left and right:
                continue  # can fit 2
            elif left or middle or right:
                result -= 1  # can fit 1
            else:
                result -= 2  # can fit 0
        return result
