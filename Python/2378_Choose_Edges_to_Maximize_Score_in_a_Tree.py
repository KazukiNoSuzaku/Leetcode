# Author: Kaustav Ghosh
# Problem: Choose Edges to Maximize Score in a Tree
# Approach: For every node keep two numbers over its subtree: free, the best score when no chosen edge touches the node, and best, the score when it may also use one edge down to a child. free is the sum of the children's best scores, and best additionally takes the most profitable child edge, swapping that child's best for its free plus the edge weight. The parents are not given in topological order, so the post-order is built with an explicit stack

class Solution(object):
    def maxScore(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(edges)
        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[edges[node][0]].append(node)
        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            stack.extend(children[node])
        free = [0] * n
        best = [0] * n
        for node in reversed(order):
            base = sum(best[c] for c in children[node])
            gain = max((free[c] + edges[c][1] - best[c] for c in children[node]), default=0)
            free[node] = base
            best[node] = base + max(gain, 0)
        return best[0]
