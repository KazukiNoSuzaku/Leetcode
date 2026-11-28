# Author: Kaustav Ghosh
# Problem: Count Nodes With the Highest Score
# Approach: Removing a node leaves one piece per child subtree plus, unless the node is the root, everything else in the tree, and that last piece's size is the whole tree minus the removed node's own subtree. So all the scores follow from the subtree sizes, which are accumulated by walking the nodes in reverse of a pre-order traversal so that every child is finished before its parent. The traversal uses an explicit stack rather than recursion because the tree can be a hundred thousand nodes deep. Each node's score is then the product of its pieces, with the piece above omitted for the root since an empty piece is not a subtree, and a single sweep keeps the largest score and how many nodes achieve it.

class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        total = len(parents)
        children = [[] for _ in range(total)]
        for node in range(1, total):
            children[parents[node]].append(node)

        order = []
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            stack.extend(children[node])

        size = [1] * total
        for node in reversed(order):
            for child in children[node]:
                size[node] += size[child]

        best = 0
        found = 0
        for node in range(total):
            score = 1
            for child in children[node]:
                score *= size[child]
            above = total - size[node]
            if above > 0:
                score *= above
            if score > best:
                best = score
                found = 1
            elif score == best:
                found += 1
        return found
