# Given 3-digit numbers encoding a complete binary tree, find the sum of all root-to-leaf paths.

# Author: Kaustav Ghosh

class Solution(object):
    def pathSum(self, nums):
        tree = {}
        for num in nums:
            depth, pos, val = num // 100, (num % 100) // 10, num % 10
            tree[(depth, pos)] = val
        res = [0]
        def dfs(depth, pos, cur):
            if (depth, pos) not in tree: return
            cur = cur * 10 + tree[(depth, pos)]
            left = (depth + 1, 2 * pos - 1)
            right = (depth + 1, 2 * pos)
            if left not in tree and right not in tree:
                res[0] += cur
            else:
                dfs(depth + 1, 2 * pos - 1, cur)
                dfs(depth + 1, 2 * pos, cur)
        dfs(1, 1, 0)
        return res[0]
