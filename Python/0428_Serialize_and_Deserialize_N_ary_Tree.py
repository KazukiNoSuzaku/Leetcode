# Serialization is the process of converting a data structure or object into a sequence
# of bits so that it can be stored or transmitted. Design an algorithm to serialize and
# deserialize an N-ary tree.

# Author: Kaustav Ghosh

from collections import deque

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for child in node.children:
                queue.append(child)
        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return None
        vals = iter(data.split(','))
        root = Node(int(next(vals)))
        queue = deque([(root, int(next(vals)))])
        while queue:
            node, count = queue.popleft()
            for _ in range(count):
                child = Node(int(next(vals)))
                child_count = int(next(vals))
                node.children.append(child)
                queue.append((child, child_count))
        return root
