# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# A -> 1, B -> 2, ..., Z -> 26, AA -> 27, AB -> 28, ...

# Example 1:
# Input: columnNumber = 1
# Output: "A"

# Example 2:
# Input: columnNumber = 28
# Output: "AB"

# Example 3:
# Input: columnNumber = 701
# Output: "ZY"

# Constraints:
# 1 <= columnNumber <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def convertToTitle(self, columnNumber):
        result = []
        while columnNumber:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))
