# Author: Kaustav Ghosh
# Problem: Minimum Score After Removals on a Tree
# Approach: Root the tree and compute each node's subtree XOR plus Euler in/out times. Removing two parent-edges (isolating subtrees of nodes a and b) yields three components whose XORs depend on whether one node is an ancestor of the other. Try all pairs of cut nodes, compute the three XORs accordingly, and minimize max-min

class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        total = 0
        for x in nums:
            total ^= x

        subxor = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = [0]

        # iterative DFS post-order for subtree XOR and Euler times
        parent = [-1] * n
        order = []
        stack = [(0, False)]
        visited = [False] * n
        while stack:
            node, processed = stack.pop()
            if processed:
                tout[node] = timer[0]
                timer[0] += 1
                x = nums[node]
                for c in adj[node]:
                    if c != parent[node]:
                        x ^= subxor[c]
                subxor[node] = x
                continue
            visited[node] = True
            tin[node] = timer[0]
            timer[0] += 1
            stack.append((node, True))
            for c in adj[node]:
                if not visited[c]:
                    parent[c] = node
                    stack.append((c, False))

        def is_ancestor(a, b):
            # is a an ancestor of b (a above b)?
            return tin[a] <= tin[b] and tout[b] <= tout[a]

        cut_nodes = [u for u in range(n) if u != 0]
        best = float('inf')
        k = len(cut_nodes)
        for i in range(k):
            a = cut_nodes[i]
            for j in range(i + 1, k):
                b = cut_nodes[j]
                if is_ancestor(a, b):
                    x1 = subxor[b]
                    x2 = subxor[a] ^ subxor[b]
                    x3 = total ^ subxor[a]
                elif is_ancestor(b, a):
                    x1 = subxor[a]
                    x2 = subxor[b] ^ subxor[a]
                    x3 = total ^ subxor[b]
                else:
                    x1 = subxor[a]
                    x2 = subxor[b]
                    x3 = total ^ subxor[a] ^ subxor[b]
                score = max(x1, x2, x3) - min(x1, x2, x3)
                if score < best:
                    best = score
        return best
