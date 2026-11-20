# Author: Kaustav Ghosh
# Problem: Find if Path Exists in Graph
# Approach: The graph is undirected, so a path exists exactly when source and destination sit in the same connected component, and reachability is all that is asked; no distances are needed. I build adjacency lists once and run a depth-first search from source with an explicit stack, marking vertices as seen when they are pushed so each is expanded at most once. The explicit stack matters because the graph may be a path of 2 * 10^5 vertices, which would exhaust Python's recursion limit. The search stops the moment destination is reached, and the degenerate case of source equal to destination is handled by testing before any edge is walked, giving O(n + e) time.

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        neighbours = [[] for _ in range(n)]
        for one, two in edges:
            neighbours[one].append(two)
            neighbours[two].append(one)

        seen = [False] * n
        seen[source] = True
        stack = [source]
        while stack:
            here = stack.pop()
            for there in neighbours[here]:
                if there == destination:
                    return True
                if not seen[there]:
                    seen[there] = True
                    stack.append(there)
        return False
