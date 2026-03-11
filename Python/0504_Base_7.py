# Given an integer num, return a string of its base 7 representation.

# Author: Kaustav Ghosh

class Solution(object):
    def convertToBase7(self, num):
        if num == 0: return '0'
        neg = num < 0
        num = abs(num)
        res = ''
        while num:
            res = str(num % 7) + res
            num //= 7
        return ('-' + res) if neg else res
