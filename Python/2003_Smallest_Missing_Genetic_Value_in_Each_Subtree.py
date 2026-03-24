# Author: Kaustav Ghosh
# Problem 2003: Smallest Missing Genetic Value in Each Subtree

class Solution(object):
    def smallestMissingValueSubtree(self, parents, nums):
        """
        :type parents: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(parents)
        result = [1] * n

        if 1 not in nums:
            return result

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        node = nums.index(1)
        visited = set()
        miss = 1

        def dfs(u):
            stack = [u]
            while stack:
                v = stack.pop()
                if v in visited:
                    continue
                visited.add(v)
                for c in children[v]:
                    stack.append(c)

        while node != -1:
            dfs(node)
            vals = {nums[v] for v in visited}
            while miss in vals:
                miss += 1
            result[node] = miss
            node = parents[node]

        return result
