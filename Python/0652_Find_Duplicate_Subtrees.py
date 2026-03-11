# Find all duplicate subtrees in a binary tree; return one node from each duplicate group.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = defaultdict(int)
        res = []
        def serialize(node):
            if not node: return '#'
            serial = '%d,%s,%s' % (node.val, serialize(node.left), serialize(node.right))
            count[serial] += 1
            if count[serial] == 2:
                res.append(node)
            return serial
        serialize(root)
        return res
