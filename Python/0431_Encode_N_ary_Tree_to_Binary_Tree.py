# Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree
# to get the original N-ary tree structure. There is no restriction on how your encode/decode
# algorithm should work. Using the left-child right-sibling representation.

# Author: Kaustav Ghosh

class Codec:
    def encode(self, root):
        if not root:
            return None
        binary_root = TreeNode(root.val)
        if root.children:
            binary_root.left = self.encode(root.children[0])
        cur = binary_root.left
        for i in range(1, len(root.children)):
            cur.right = self.encode(root.children[i])
            cur = cur.right
        return binary_root

    def decode(self, root):
        if not root:
            return None
        node = Node(root.val, [])
        cur = root.left
        while cur:
            node.children.append(self.decode(cur))
            cur = cur.right
        return node
