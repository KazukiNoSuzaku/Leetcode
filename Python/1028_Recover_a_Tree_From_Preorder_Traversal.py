# Recover a binary tree from its preorder traversal string where dashes indicate depth.

# Author: Kaustav Ghosh

class Solution(object):
    def recoverFromPreorder(self, traversal):
        stack = []
        i = 0
        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            val = 0
            while i < len(traversal) and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            node = TreeNode(val)
            while len(stack) > depth:
                stack.pop()
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]
