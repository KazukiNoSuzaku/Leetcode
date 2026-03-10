# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer.
# You must not use any built-in library function, such as sqrt.

# Example 1:
# Input: num = 16
# Output: true

# Example 2:
# Input: num = 14
# Output: false

# Constraints:
# 1 <= num <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def isPerfectSquare(self, num):
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
