# Author: Kaustav Ghosh
# Problem: Maximum Number of Groups Entering a Competition
# Approach: Sorting the grades lets group i take the next i + 1 students, which makes every group both larger and higher-scoring than the one before, so the only limit is the total size: the answer is the largest k with k * (k + 1) / 2 <= n

class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        n = len(grades)
        k = int(((8 * n + 1) ** 0.5 - 1) // 2)
        while (k + 1) * (k + 2) // 2 <= n:
            k += 1
        while k * (k + 1) // 2 > n:
            k -= 1
        return k
