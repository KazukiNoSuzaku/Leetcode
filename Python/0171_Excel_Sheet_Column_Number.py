# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.
# A -> 1, B -> 2, ..., Z -> 26, AA -> 27, AB -> 28, ...

# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701

# Constraints:
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for c in columnTitle:
            result = result * 26 + (ord(c) - ord('A') + 1)
        return result
