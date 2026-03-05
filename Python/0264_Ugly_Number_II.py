# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.

# Example 1:
# Input: n = 10
# Output: 12

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
# 1 <= n <= 1690

# Author: Kaustav Ghosh

class Solution(object):
    def nthUglyNumber(self, n):
        ugly = [1] * n
        i2 = i3 = i5 = 0
        for i in range(1, n):
            next2 = ugly[i2] * 2
            next3 = ugly[i3] * 3
            next5 = ugly[i5] * 5
            ugly[i] = min(next2, next3, next5)
            if ugly[i] == next2: i2 += 1
            if ugly[i] == next3: i3 += 1
            if ugly[i] == next5: i5 += 1
        return ugly[-1]
