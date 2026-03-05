# Given an integer num, repeatedly add all its digits until the result has only one digit,
# and return it.

# Example 1:
# Input: num = 38
# Output: 2
# Explanation: 3 + 8 = 11, 1 + 1 = 2

# Example 2:
# Input: num = 0
# Output: 0

# Constraints:
# 0 <= num <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
