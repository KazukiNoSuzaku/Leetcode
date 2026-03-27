# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

from collections import deque

class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        n = len(favorite)
        in_degree = [0] * n
        for f in favorite:
            in_degree[f] += 1

        # Topological sort to find chain lengths into cycles
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        depth = [1] * n
        while queue:
            node = queue.popleft()
            nxt = favorite[node]
            depth[nxt] = max(depth[nxt], depth[node] + 1)
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

        # Find cycles
        max_cycle = 0
        chain_sum = 0
        visited = [False] * n
        for i in range(n):
            if visited[i] or in_degree[i] == 0:
                continue
            # Trace cycle
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = favorite[j]
                cycle_len += 1
            if cycle_len == 2:
                # 2-cycle: can extend with chains
                chain_sum += depth[i] + depth[favorite[i]]
            else:
                max_cycle = max(max_cycle, cycle_len)

        return max(max_cycle, chain_sum)
