# Author: Kaustav Ghosh
# Problem: Reformat Phone Number
# Approach: Strip to digits, chunk in threes while more than 4 remain, then split the tail (4 -> 2+2, else one block), joined by dashes

class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        digits = [c for c in number if c.isdigit()]
        blocks = []
        i, n = 0, len(digits)
        while n - i > 4:
            blocks.append(''.join(digits[i:i + 3]))
            i += 3
        if n - i == 4:
            blocks.append(''.join(digits[i:i + 2]))
            blocks.append(''.join(digits[i + 2:i + 4]))
        else:
            blocks.append(''.join(digits[i:]))
        return '-'.join(blocks)
