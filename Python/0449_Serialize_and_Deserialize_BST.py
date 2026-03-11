# Serialization is converting a data structure or object into a sequence of bits.
# Design an algorithm to serialize and deserialize a binary search tree.
# The encoded string should be as compact as possible.

# Author: Kaustav Ghosh

class Codec:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return
            vals.append(node.val)
            preorder(node.left)
            preorder(node.right)
        vals = []
        preorder(root)
        return ','.join(map(str, vals))

    def deserialize(self, data):
        if not data:
            return None
        vals = iter(map(int, data.split(',')))

        def build(min_val, max_val):
            val = next(vals, None)
            if val is None:
                return None
            if not (min_val < val < max_val):
                # put back by using a nested iterator trick via list
                return None
            node = TreeNode(val)
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            return node

        # Use list to allow lookahead
        vals_list = list(map(int, data.split(',')))
        idx = [0]

        def rebuild(mn, mx):
            if idx[0] >= len(vals_list) or not (mn < vals_list[idx[0]] < mx):
                return None
            val = vals_list[idx[0]]
            idx[0] += 1
            node = TreeNode(val)
            node.left = rebuild(mn, val)
            node.right = rebuild(val, mx)
            return node

        return rebuild(float('-inf'), float('inf'))
