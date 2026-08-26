# Author: Kaustav Ghosh
# Problem: Count the Hidden Sequences
# Approach: Fixing the first element at 0, the running prefix sums of differences give every element's offset. The whole sequence fits in [lower, upper] iff the first element lies in [lower - min_prefix, upper - max_prefix]; the count is the size of that range

class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = 0
        lo = hi = 0
        for d in differences:
            prefix += d
            lo = min(lo, prefix)
            hi = max(hi, prefix)
        return max(0, (upper - hi) - (lower - lo) + 1)
