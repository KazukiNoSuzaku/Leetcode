# Author: Kaustav Ghosh
# Problem: Number of Nodes in the Sub-Tree With the Same Label
# Approach: Root the tree at 0 and walk it in post-order with an explicit stack, carrying a 26-slot tally of labels up from each subtree. A node's answer is its own label's tally once its children have been folded in, and a child's tally is released after merging to keep memory flat

class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        parent = [-1] * n
        order = []
        seen = [False] * n
        seen[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            for nxt in graph[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    parent[nxt] = node
                    stack.append(nxt)

        tallies = [None] * n
        answer = [0] * n
        for node in reversed(order):
            if tallies[node] is None:
                tallies[node] = [0] * 26
            own = ord(labels[node]) - ord('a')
            tallies[node][own] += 1
            answer[node] = tallies[node][own]
            above = parent[node]
            if above != -1:
                if tallies[above] is None:
                    tallies[above] = [0] * 26
                target = tallies[above]
                for i, value in enumerate(tallies[node]):
                    if value:
                        target[i] += value
                tallies[node] = None
        return answer
