# Author: Kaustav Ghosh
# Problem: Delete Duplicate Folders in System
# Approach: Build the folder tree, then give every non-empty subtree a canonical serialization built from its sorted children. Any serialization shared by two or more (non-root) folders marks all of them for deletion. Emit the paths of folders not inside a marked subtree

from collections import Counter

class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        root = {}
        for p in paths:
            cur = root
            for name in p:
                cur = cur.setdefault(name, {})

        serial_of = {}

        def serialize(node):
            parts = []
            for name in sorted(node):
                parts.append(name + "(" + serialize(node[name]) + ")")
            s = "".join(parts)
            serial_of[id(node)] = s
            return s

        serialize(root)

        cnt = Counter()

        def count(node, is_root):
            if node and not is_root:
                cnt[serial_of[id(node)]] += 1
            for name in node:
                count(node[name], False)

        count(root, True)

        marked = set()

        def mark(node, is_root):
            if node and not is_root and cnt[serial_of[id(node)]] >= 2:
                marked.add(id(node))
            for name in node:
                mark(node[name], False)

        mark(root, True)

        result = []

        def emit(node, path):
            for name in sorted(node):
                child = node[name]
                if id(child) in marked:
                    continue
                result.append(path + [name])
                emit(child, path + [name])

        emit(root, [])
        return result
