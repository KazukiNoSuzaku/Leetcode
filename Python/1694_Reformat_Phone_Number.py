# Author: Kaustav Ghosh
# https://leetcode.com/problems/reformat-phone-number/

class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        digits = number.replace(' ', '').replace('-', '')
        result = []
        i = 0
        while len(digits) - i > 4:
            result.append(digits[i:i + 3])
            i += 3
        remaining = len(digits) - i
        if remaining <= 3:
            result.append(digits[i:])
        else:  # remaining == 4
            result.append(digits[i:i + 2])
            result.append(digits[i + 2:])
        return '-'.join(result)
