# Author: Kaustav Ghosh
# Problem: Maximum Number of Weeks for Which You Can Work
# Approach: The only rule is that two consecutive weeks cannot touch the same project, so the largest project is the bottleneck: its milestones have to be separated by milestones from the others. If the rest of the work is at least as large as the biggest project minus one, the weeks can be interleaved so nothing is ever wasted and every milestone gets done, giving the full total. Otherwise the biggest project runs out of partners, and the best schedule alternates it with every other milestone and then takes one final week from it, finishing 2 * rest + 1 milestones before stalling. Both branches are decided by one pass computing the total and the maximum.

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
