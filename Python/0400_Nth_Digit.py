# Given an integer n, return the nth digit of the infinite integer sequence
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

# Author: Kaustav Ghosh

class Solution(object):
    def findNthDigit(self, n):
        digits = 1
        start = 1
        count = 9
        while n > digits * count:
            n -= digits * count
            digits += 1
            start *= 10
            count *= 10
        num = start + (n - 1) // digits
        return int(str(num)[(n - 1) % digits])
