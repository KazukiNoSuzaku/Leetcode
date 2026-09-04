# Author: Kaustav Ghosh
# Problem: Longest Path With Different Adjacent Characters
# Approach: Root the tree and post-order DFS. For each node, look at children whose character differs from it; the longest downward chain through the node is 1 plus the best such child chain, and the longest path bending at the node is 1 plus the top two child chains. Track the global maximum node count. An explicit stack avoids recursion limits

class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        best_down = [1] * n
        ans = 1

        # iterative post-order
        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            for ch in children[node]:
                stack.append(ch)

        for node in reversed(order):
            top1 = top2 = 0  # two longest valid child chains
            for ch in children[node]:
                if s[ch] != s[node]:
                    d = best_down[ch]
                    if d > top1:
                        top2 = top1
                        top1 = d
                    elif d > top2:
                        top2 = d
            best_down[node] = top1 + 1
            ans = max(ans, top1 + top2 + 1)
        return ans
