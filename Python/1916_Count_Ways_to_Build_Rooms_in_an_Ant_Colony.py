# Author: Kaustav Ghosh
# Problem: Count Ways to Build Rooms in an Ant Colony
# Approach: A room can only be built after the room it hangs off, so a valid order is exactly a linear extension of the tree, and the number of those is n factorial divided by the product of all the subtree sizes. The reason is that among the orderings of a subtree's nodes only the fraction where its root comes first is valid, and that fraction is one over its size, applied independently at every node. Subtree sizes are accumulated by walking the nodes in reverse breadth-first order so each node is finished before its parent needs it, which avoids recursion on a colony that may be a chain of a hundred thousand rooms. The division is done with a modular inverse of the single accumulated product rather than one inverse per node.

class Solution(object):
    def waysToBuildRooms(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(prevRoom)

        children = [[] for _ in range(n)]
        for room in range(1, n):
            children[prevRoom[room]].append(room)

        order = [0]
        for room in order:
            order.extend(children[room])

        size = [1] * n
        product = 1
        for room in reversed(order):
            parent = prevRoom[room]
            if parent >= 0:
                size[parent] += size[room]
            product = product * size[room] % MOD

        ways = 1
        for value in range(2, n + 1):
            ways = ways * value % MOD
        return ways * pow(product, MOD - 2, MOD) % MOD
