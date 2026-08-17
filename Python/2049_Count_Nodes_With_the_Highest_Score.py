# Author: Kaustav Ghosh
# Problem: Count Nodes With the Highest Score
# Approach: Compute every subtree size once. Removing a node splits the tree into its child subtrees plus the remaining upper part (n - size[node]); the score is the product of the non-empty parts. Count how many nodes reach the maximum score

class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n = len(parents)
        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[parents[node]].append(node)

        size = [1] * n
        # iterative post-order so large trees don't overflow recursion
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for c in children[u]:
                stack.append(c)
        for u in reversed(order):
            for c in children[u]:
                size[u] += size[c]

        best = 0
        count = 0
        for node in range(n):
            score = 1
            for c in children[node]:
                score *= size[c]
            upper = n - size[node]
            if upper > 0:
                score *= upper
            if score > best:
                best = score
                count = 1
            elif score == best:
                count += 1
        return count
