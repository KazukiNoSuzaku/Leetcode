import sys
sys.setrecursionlimit(100000)

# Premium problem
# Tree DP: dp[node] = (unmatched, matched) max scores in subtree
# unmatched: node not connected to any chosen edge on its parent side
# matched: node connected upward via one child edge

class Solution:
    def maximumScore(self, edges: list[list[int]]) -> int:
        n = len(edges)
        children = [[] for _ in range(n)]
        for child, (parent, weight) in enumerate(edges):
            if parent != -1:
                children[parent].append((child, weight))

        def dfs(node):
            unmatched = 0
            best_gain = 0  # best gain from matching node with one child
            for child, w in children[node]:
                child_un, child_mat = dfs(child)
                unmatched += max(child_un, child_mat)
                # gain of picking edge (node, child): w + child_un - max(child_un, child_mat)
                best_gain = max(best_gain, w + child_un - max(child_un, child_mat))
            return unmatched, unmatched + best_gain

        un, mat = dfs(0)
        return max(un, mat)
