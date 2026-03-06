# Given a string num which represents an integer, return true if num is a strobogrammatic number.
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (upside down).

# Example 1:
# Input: num = "69"
# Output: true

# Example 2:
# Input: num = "88"
# Output: true

# Constraints:
# 1 <= num.length <= 50
# num consists of only digits.
# num does not have leading zeros except for zero itself.

# Author: Kaustav Ghosh

class Solution(object):
    def isStrobogrammatic(self, num):
        pairs = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if num[lo] not in pairs or pairs[num[lo]] != num[hi]:
                return False
            lo += 1
            hi -= 1
        return True
