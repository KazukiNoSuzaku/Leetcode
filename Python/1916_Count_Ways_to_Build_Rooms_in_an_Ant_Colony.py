# Author: Kaustav Ghosh
# Problem: Count Ways to Build Rooms in an Ant Colony
# Approach: A valid build order is a topological order of the tree with the root first. The number of such orders is n! / product(subtree_size[v]). Since prevRoom[i] < i, compute subtree sizes bottom-up and combine with modular inverse

class Solution(object):
    def waysToBuildRooms(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(prevRoom)

        size = [1] * n
        for i in range(n - 1, 0, -1):          # children have larger index than parents
            size[prevRoom[i]] += size[i]

        # factorial of n
        fact = 1
        for i in range(2, n + 1):
            fact = fact * i % MOD

        denom = 1
        for s in size:
            denom = denom * s % MOD

        return fact * pow(denom, MOD - 2, MOD) % MOD
