# Author: Kaustav Ghosh
# Problem: Largest Combination With Bitwise AND Greater Than Zero
# Approach: A subset has a positive AND exactly when all its members share some set bit. For each bit position, the largest such subset is all numbers with that bit set, so the answer is the maximum count of numbers sharing any single bit

class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        best = 0
        for bit in range(24):
            count = sum(1 for x in candidates if (x >> bit) & 1)
            best = max(best, count)
        return best
