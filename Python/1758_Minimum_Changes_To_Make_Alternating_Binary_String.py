# Author: Kaustav Ghosh
# Problem: Minimum Changes To Make Alternating Binary String
# Approach: Only two alternating targets exist ("0101..." and "1010..."), and they are complements; count mismatches against one, the other costs n minus that

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        mismatches = sum(1 for i, c in enumerate(s) if int(c) != i % 2)
        return min(mismatches, len(s) - mismatches)
