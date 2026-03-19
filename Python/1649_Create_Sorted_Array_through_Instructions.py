# Author: Kaustav Ghosh
# https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        m = max(instructions) + 2
        tree = [0] * m

        def update(i):
            while i < m:
                tree[i] += 1
                i += i & (-i)

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        cost = 0
        for i, num in enumerate(instructions):
            left = query(num - 1)
            right = i - query(num)
            cost = (cost + min(left, right)) % MOD
            update(num)
        return cost
