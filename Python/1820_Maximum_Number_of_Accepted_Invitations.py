# Author: Kaustav Ghosh
# Problem: Maximum Number of Accepted Invitations
# Approach: Boys on one side, girls on the other and an invitation only where the grid allows it: this is a maximum matching in a bipartite graph. Each boy is processed in turn and offered a girl; if she is already taken, the boy currently matched to her is asked to move elsewhere, and that request cascades along an augmenting path. Finding such a path raises the matching by exactly one, and failing to find one means this boy cannot be added without displacing someone, which is the stopping condition that makes the greedy pass optimal. The visited set is reset per boy so each girl is considered at most once inside a single search.

class Solution(object):
    def maximumInvitations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        girls = len(grid[0])
        partner = [-1] * girls

        def offer(boy, asked):
            for girl in range(girls):
                if not grid[boy][girl] or girl in asked:
                    continue
                asked.add(girl)
                if partner[girl] < 0 or offer(partner[girl], asked):
                    partner[girl] = boy
                    return True
            return False

        accepted = 0
        for boy in range(len(grid)):
            if offer(boy, set()):
                accepted += 1
        return accepted
