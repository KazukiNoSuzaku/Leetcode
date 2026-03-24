# Author: Kaustav Ghosh
# https://leetcode.com/problems/delete-duplicate-folders-in-system/

from collections import defaultdict

class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        # Build trie
        root = {}
        for path in paths:
            node = root
            for folder in path:
                if folder not in node:
                    node[folder] = {}
                node = node[folder]

        # Serialize subtrees and find duplicates
        serial_count = defaultdict(int)
        serial_map = {}

        def serialize(node):
            if not node:
                return ""
            parts = []
            for name in sorted(node):
                parts.append("(" + name + serialize(node[name]) + ")")
            s = "".join(parts)
            if s:
                serial_count[s] += 1
                serial_map[id(node)] = s
            return s

        serialize(root)

        # Collect valid paths
        result = []

        def collect(node, path):
            for name in node:
                child = node[name]
                child_serial = serial_map.get(id(child), "")
                if child_serial and serial_count[child_serial] > 1:
                    continue
                path.append(name)
                result.append(list(path))
                collect(child, path)
                path.pop()

        collect(root, [])
        return result
