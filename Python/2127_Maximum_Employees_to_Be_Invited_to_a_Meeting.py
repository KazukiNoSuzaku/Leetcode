# Author: Kaustav Ghosh
# Problem: Maximum Employees to Be Invited to a Meeting
# Approach: Each employee points to one favorite, forming a functional graph. Either the table is one cycle of length >= 3 (seat the whole cycle), or it is built from mutual pairs (2-cycles) each extended by the longest chains feeding into its two members. The answer is the larger of the longest big cycle and the summed 2-cycle chains

from collections import deque

class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        n = len(favorite)
        indeg = [0] * n
        for f in favorite:
            indeg[f] += 1

        # longest chain ending at each node (tree branches), via topological peeling
        depth = [1] * n
        q = deque(i for i in range(n) if indeg[i] == 0)
        while q:
            u = q.popleft()
            v = favorite[u]
            depth[v] = max(depth[v], depth[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        visited = [False] * n
        longest_cycle = 0
        two_cycle_total = 0
        for i in range(n):
            if visited[i] or indeg[i] == 0:
                continue
            # walk the cycle starting at i
            cycle = []
            node = i
            while not visited[node]:
                visited[node] = True
                cycle.append(node)
                node = favorite[node]
            length = len(cycle)
            if length == 2:
                a, b = cycle
                two_cycle_total += depth[a] + depth[b]
            else:
                longest_cycle = max(longest_cycle, length)

        return max(longest_cycle, two_cycle_total)
