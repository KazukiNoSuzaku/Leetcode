# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-the-hidden-sequences/

class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = 0
        min_prefix = 0
        max_prefix = 0
        for d in differences:
            prefix += d
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)

        # hidden[0] must satisfy:
        # hidden[0] + min_prefix >= lower
        # hidden[0] + max_prefix <= upper
        lo = lower - min_prefix
        hi = upper - max_prefix
        return max(0, hi - lo + 1)
