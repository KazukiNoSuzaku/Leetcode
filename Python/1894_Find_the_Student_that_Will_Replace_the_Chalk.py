# Author: Kaustav Ghosh
# Problem: Find the Student that Will Replace the Chalk
# Approach: Each full sweep of the class consumes the same fixed total, so however many complete sweeps the chalk allows are irrelevant to who runs out: reducing k modulo that total leaves the position within a single sweep unchanged. From there one pass subtracts each student's usage until the chalk cannot cover the next one, which is the answer. The modulo is what keeps this linear despite k reaching a billion.

class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        k %= sum(chalk)
        for student, needed in enumerate(chalk):
            if k < needed:
                return student
            k -= needed
        return 0
