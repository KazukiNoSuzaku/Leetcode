# Author: Kaustav Ghosh
# Problem: Maximum Number of Weeks for Which You Can Work
# Approach: You can complete everything unless one project dominates. If the largest pile exceeds the rest plus one, it bottlenecks: you finish 2*rest+1 weeks. Otherwise all milestones can be interleaved

class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        total = sum(milestones)
        biggest = max(milestones)
        rest = total - biggest
        if biggest > rest + 1:
            return 2 * rest + 1
        return total
