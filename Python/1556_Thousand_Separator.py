# Author: Kaustav Ghosh
# Problem: 1556 - Thousand Separator
# Approach: Insert dots every 3 digits from right

class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)
        result = []
        for i, c in enumerate(s):
            if i > 0 and (len(s) - i) % 3 == 0:
                result.append('.')
            result.append(c)
        return ''.join(result)
