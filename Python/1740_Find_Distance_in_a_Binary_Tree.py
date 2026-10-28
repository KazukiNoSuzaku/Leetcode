# Author: Kaustav Ghosh
# Problem: Find Distance in a Binary Tree
# Approach: The only route between two nodes in a tree runs up to their lowest common ancestor and back down, so the distance is the sum of their depths minus twice the ancestor's. Rather than finding the ancestor and the depths separately, I collect each node's path from the root once and then strip their shared prefix: whatever remains of the two paths is precisely the two legs of the journey, which also makes the case of a node paired with itself fall out as zero. The search for the paths is an explicit stack carrying the path so far, so a tree of ten thousand nodes arranged as a chain cannot overflow the recursion limit.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def findDistance(self, root, p, q):
        """
        :type root: Optional[TreeNode]
        :type p: int
        :type q: int
        :rtype: int
        """
        def path_to(target):
            stack = [(root, [])]
            while stack:
                node, trail = stack.pop()
                if node is None:
                    continue
                here = trail + [node.val]
                if node.val == target:
                    return here
                stack.append((node.left, here))
                stack.append((node.right, here))
            return []

        first = path_to(p)
        second = path_to(q)

        shared = 0
        while shared < len(first) and shared < len(second) and first[shared] == second[shared]:
            shared += 1
        return (len(first) - shared) + (len(second) - shared)
