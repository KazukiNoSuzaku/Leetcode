# Author: Kaustav Ghosh
# Problem: Maximum Number of Accepted Invitations (Premium)
# Approach: This is maximum bipartite matching between boys and girls; run Kuhn's augmenting-path algorithm, letting each boy claim a girl or bump an earlier match that can relocate

class Solution(object):
    def maximumInvitations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        match_of_girl = [-1] * n

        def augment(boy, seen):
            for girl in range(n):
                if grid[boy][girl] and not seen[girl]:
                    seen[girl] = True
                    if match_of_girl[girl] == -1 or augment(match_of_girl[girl], seen):
                        match_of_girl[girl] = boy
                        return True
            return False

        matches = 0
        for boy in range(m):
            if augment(boy, [False] * n):
                matches += 1
        return matches
