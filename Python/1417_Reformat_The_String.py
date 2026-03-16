# Author: Kaustav Ghosh
# Problem: Reformat The String
# Approach: Alternate digits and letters

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits = [c for c in s if c.isdigit()]
        letters = [c for c in s if c.isalpha()]
        if abs(len(digits) - len(letters)) > 1:
            return ""
        if len(digits) < len(letters):
            digits, letters = letters, digits
        result = []
        for i in range(len(letters)):
            result.append(digits[i])
            result.append(letters[i])
        if len(digits) > len(letters):
            result.append(digits[-1])
        return ''.join(result)
