# Author: Kaustav Ghosh
# Problem: Tree of Coprimes
# Approach: Values never exceed 50, so instead of walking up the ancestor chain each node only needs the deepest ancestor holding each of the 50 possible values. One stack per value, pushed on the way down and popped on the way back up, keeps exactly the current root-to-node path, and the top of each stack is the deepest ancestor with that value. For a node the answer is then the deepest top among the values coprime to its own, a check over at most 50 precomputed candidates. The traversal is an explicit stack with an exit marker so that a path of 100000 nodes cannot overflow recursion.

class Solution(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from math import gcd

        n = len(nums)
        adjacency = [[] for _ in range(n)]
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        coprimes = [[v for v in range(1, 51) if gcd(u, v) == 1] for u in range(51)]
        chains = [[] for _ in range(51)]
        answer = [-1] * n
        parent = [-1] * n

        stack = [(0, 0, False)]
        while stack:
            node, depth, leaving = stack.pop()
            if leaving:
                chains[nums[node]].pop()
                continue

            deepest = -1
            for value in coprimes[nums[node]]:
                if chains[value] and chains[value][-1][0] > deepest:
                    deepest, answer[node] = chains[value][-1]

            chains[nums[node]].append((depth, node))
            stack.append((node, depth, True))
            for child in adjacency[node]:
                if child != parent[node]:
                    parent[child] = node
                    stack.append((child, depth + 1, False))
        return answer
