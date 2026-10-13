# Author: Kaustav Ghosh
# Problem: Rearrange Spaces Between Words
# Approach: The total number of spaces is fixed, so with w words there are w-1 gaps to fill as evenly as possible: each gap takes the quotient and whatever does not divide evenly is parked at the end, which is what the problem asks for. The single-word case has no gaps at all and so takes every space as trailing, and it has to be handled separately or the division would be by zero.

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
        gap, leftover = divmod(spaces, len(words) - 1)
        return (' ' * gap).join(words) + ' ' * leftover
