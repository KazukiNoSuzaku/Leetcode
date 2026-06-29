# Author: Kaustav Ghosh
# Problem: Thousand Separator
# Approach: Use Python's comma grouping format, then swap the commas for dots

class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        return format(n, ',').replace(',', '.')
