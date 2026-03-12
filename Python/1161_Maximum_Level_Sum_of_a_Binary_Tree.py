# Author: Kaustav Ghosh
# BFS level sums, return minimum level with maximum sum

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        queue = deque([root])
        max_sum = float('-inf')
        result = 1
        level = 0
        while queue:
            level += 1
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                result = level
        return result
