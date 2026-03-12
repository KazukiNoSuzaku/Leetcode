# Author: Kaustav Ghosh
# 1059. All Paths from Source Lead to Destination
# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # destination must have no outgoing edges
        if graph[destination]:
            return False

        # 0 = unvisited, 1 = visiting, 2 = done
        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                return False  # cycle
            if state[node] == 2:
                return True
            state[node] = 1
            if not graph[node]:
                # leaf node must be destination
                state[node] = 2
                return node == destination
            for nb in graph[node]:
                if not dfs(nb):
                    return False
            state[node] = 2
            return True

        return dfs(source)
