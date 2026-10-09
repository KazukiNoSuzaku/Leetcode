# Author: Kaustav Ghosh
# Problem: Thousand Separator
# Approach: Walk the digits from the right, emitting a dot every third one, then reverse the result

class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        digits = str(n)
        pieces = []
        for count, ch in enumerate(reversed(digits)):
            if count and count % 3 == 0:
                pieces.append('.')
            pieces.append(ch)
        return "".join(reversed(pieces))
