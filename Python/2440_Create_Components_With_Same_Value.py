# Author: Kaustav Ghosh
# Problem: Create Components With Same Value
# Approach: If the tree is cut into c components each must sum to total / c, so only divisors of the total are worth testing, and never one below the largest single value. For a candidate target, accumulate sums upward in post-order: a subtree that reaches the target exactly is cut off and contributes nothing further, while overshooting rules the target out. The first workable c, tried from many components downward, needs c - 1 deletions

class Solution(object):
    def componentValue(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        order = []
        parent = [-1] * n
        stack = [0]
        seen = [False] * n
        seen[0] = True
        while stack:
            node = stack.pop()
            order.append(node)
            for nxt in graph[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    parent[nxt] = node
                    stack.append(nxt)

        def works(target):
            carried = nums[:]
            for node in reversed(order):
                if carried[node] == target:
                    carried[node] = 0
                elif carried[node] > target:
                    return False
                if parent[node] != -1:
                    carried[parent[node]] += carried[node]
            return carried[0] == 0

        total = sum(nums)
        biggest = max(nums)
        for components in range(n, 1, -1):
            if total % components:
                continue
            if total // components < biggest:
                continue
            if works(total // components):
                return components - 1
        return 0
