# Author: Kaustav Ghosh
# Problem: Create Sorted Array through Instructions
# Approach: A Fenwick tree over values gives, for each insertion, how many earlier elements are strictly smaller and strictly larger; the cost is the min of the two

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        m = max(instructions)
        tree = [0] * (m + 1)

        def update(i):
            while i <= m:
                tree[i] += 1
                i += i & -i

        def query(i):  # count of inserted values <= i
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & -i
            return total

        cost = 0
        for placed, x in enumerate(instructions):
            smaller = query(x - 1)
            larger = placed - query(x)
            cost = (cost + min(smaller, larger)) % MOD
            update(x)
        return cost
