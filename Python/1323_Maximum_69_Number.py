# Given a number made of only 6s and 9s, change at most one digit to get the maximum value.

# Author: Kaustav Ghosh

class Solution(object):
    def maximum69Number(self, num):
        return int(str(num).replace('6', '9', 1))
