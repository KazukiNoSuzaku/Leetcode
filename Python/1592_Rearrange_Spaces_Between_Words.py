# Author: Kaustav Ghosh
# Problem: Rearrange Spaces Between Words
# Approach: Count words and total spaces; distribute spaces evenly between words and dump any remainder at the end

class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * spaces
        gap, extra = divmod(spaces, len(words) - 1)
        return (' ' * gap).join(words) + ' ' * extra
