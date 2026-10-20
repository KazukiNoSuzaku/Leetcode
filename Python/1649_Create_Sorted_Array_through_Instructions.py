# Author: Kaustav Ghosh
# Problem: Create Sorted Array through Instructions
# Approach: Each insertion's cost asks how many already-inserted values are strictly smaller and how many are strictly larger, so the structure needed is one that counts values in a range while supporting insertions, which is exactly a Fenwick tree over the value range. For each instruction I read the count below it, derive the count above it as the number inserted so far minus those below minus those equal to it, and take the smaller; deriving the upper count rather than querying it again halves the work and automatically excludes equal values from both sides, which is what "strictly" requires.

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        limit = max(instructions)
        tree = [0] * (limit + 1)

        def add(index):
            while index <= limit:
                tree[index] += 1
                index += index & -index

        def total_upto(index):
            running = 0
            while index > 0:
                running += tree[index]
                index -= index & -index
            return running

        cost = 0
        for placed, value in enumerate(instructions):
            at_or_below = total_upto(value)
            below = total_upto(value - 1)
            above = placed - at_or_below
            cost += below if below < above else above
            add(value)
        return cost % MOD
