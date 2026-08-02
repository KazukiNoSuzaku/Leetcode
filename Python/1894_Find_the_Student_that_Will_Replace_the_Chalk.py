# Author: Kaustav Ghosh
# Problem: Find the Student that Will Replace the Chalk
# Approach: One full round consumes the total chalk, so reduce k mod total, then walk students subtracting until the remainder is smaller than a student's need

class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        k %= sum(chalk)
        for i, need in enumerate(chalk):
            if k < need:
                return i
            k -= need
        return 0
