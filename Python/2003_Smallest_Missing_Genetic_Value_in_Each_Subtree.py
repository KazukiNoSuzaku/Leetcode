# Author: Kaustav Ghosh
# Problem: Smallest Missing Genetic Value in Each Subtree
# Approach: Any subtree not containing the value 1 is missing 1. Only ancestors of the node holding 1 can have a larger answer. Walk from that node up to the root, accumulating each subtree's values (skipping the already-processed child) and advancing the smallest missing value

class Solution(object):
    def smallestMissingValueSubtree(self, parents, nums):
        """
        :type parents: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(parents)
        ans = [1] * n
        if 1 not in nums:
            return ans

        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[parents[node]].append(node)

        seen = set()
        node = nums.index(1)
        blocked = -1
        miss = 1
        while node != -1:
            stack = [node]
            while stack:
                x = stack.pop()
                seen.add(nums[x])
                for c in children[x]:
                    if c != blocked:
                        stack.append(c)
            while miss in seen:
                miss += 1
            ans[node] = miss
            blocked = node
            node = parents[node]
        return ans
