# Author: Kaustav Ghosh
# Problem: Reformat Phone Number
# Approach: Spaces and dashes carry no information, so they are stripped first and the problem reduces to cutting a run of digits into blocks. Blocks of three are taken greedily, but only while more than four digits remain: stopping at that threshold is what prevents a final block of a single digit, since four left over become two and two while two or three left over form one final block. Deciding the split by looking ahead rather than fixing it afterwards keeps the rule in one place.

class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        digits = [ch for ch in number if ch.isdigit()]
        blocks = []
        i = 0
        while len(digits) - i > 4:
            blocks.append(''.join(digits[i:i + 3]))
            i += 3
        remaining = len(digits) - i
        if remaining == 4:
            blocks.append(''.join(digits[i:i + 2]))
            blocks.append(''.join(digits[i + 2:i + 4]))
        else:
            blocks.append(''.join(digits[i:]))
        return '-'.join(blocks)
