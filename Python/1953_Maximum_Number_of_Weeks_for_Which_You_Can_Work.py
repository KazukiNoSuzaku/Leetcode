# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        total = sum(milestones)
        max_val = max(milestones)
        rest = total - max_val
        if max_val > rest + 1:
            return 2 * rest + 1
        return total
