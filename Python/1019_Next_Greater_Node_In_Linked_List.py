# For each node in a linked list, find the value of the next greater node.

# Author: Kaustav Ghosh

class Solution(object):
    def nextLargerNodes(self, head):
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        res = [0] * len(vals)
        stack = []
        for i, v in enumerate(vals):
            while stack and vals[stack[-1]] < v:
                res[stack.pop()] = v
            stack.append(i)
        return res
