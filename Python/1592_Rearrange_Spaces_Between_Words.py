# Author: Kaustav Ghosh
# Problem: 1592 - Rearrange Spaces Between Words
# Approach: Distribute spaces evenly between words, remainder at end

class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        words = text.split()
        spaces = text.count(' ')

        if len(words) == 1:
            return words[0] + ' ' * spaces

        gap = spaces // (len(words) - 1)
        remainder = spaces % (len(words) - 1)
        return (' ' * gap).join(words) + ' ' * remainder
