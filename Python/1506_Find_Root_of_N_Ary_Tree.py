# Find the root of an N-ary tree given all nodes in any order.
# The root is the node that never appears as a child.

# Author: Kaustav Ghosh

class Solution(object):
    def findRoot(self, tree):
        seen_as_child = set()
        for node in tree:
            for child in node.children:
                seen_as_child.add(child.val)
        for node in tree:
            if node.val not in seen_as_child:
                return node
