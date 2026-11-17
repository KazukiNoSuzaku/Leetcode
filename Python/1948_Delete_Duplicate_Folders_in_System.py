# Author: Kaustav Ghosh
# Problem: Delete Duplicate Folders in System
# Approach: Two folders are identical exactly when their subtrees, read as nested sets of named children, are the same, so I build a trie of the paths and then give every folder a canonical signature: the sorted concatenation of each child's name wrapped around that child's own signature. Sorting makes the signature independent of the order the paths arrived in, and nesting makes it depend on the whole subtree, so two folders share a signature if and only if they are identical in the problem's sense. Counting signatures across the whole tree then identifies which ones occur more than once, and a second walk emits every path that does not pass through such a folder, pruning the entire subtree at the first marked folder. Both walks use explicit stacks because paths may be 500 deep, and the signature pass is a post-order walk so a folder is only signed after all of its children are. The imaginary root is signed too, since its children need it, but it is left out of the tally because it is not a folder and so can never be deleted.

class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        root = {}
        for path in paths:
            at = root
            for name in path:
                at = at.setdefault(name, {})

        signature = {}
        seen = {}

        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node)
            for child in node.values():
                stack.append(child)

        for node in reversed(order):
            mark = "".join(sorted("(" + name + signature[id(child)] + ")"
                                  for name, child in node.items()))
            signature[id(node)] = mark
            if mark and node is not root:
                seen[mark] = seen.get(mark, 0) + 1

        kept = []
        stack = [(root, [])]
        while stack:
            node, prefix = stack.pop()
            for name, child in node.items():
                mark = signature[id(child)]
                if mark and seen[mark] > 1:
                    continue
                path = prefix + [name]
                kept.append(path)
                stack.append((child, path))

        return kept
