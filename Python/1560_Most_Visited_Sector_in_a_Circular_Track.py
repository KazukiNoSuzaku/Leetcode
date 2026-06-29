# Author: Kaustav Ghosh
# Problem: Most Visited Sector in a Circular Track
# Approach: Only the first and last marks matter; the most visited sectors are those on the arc from start to end going forward

class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        # wraps past sector n: cover 1..end then start..n
        return list(range(1, end + 1)) + list(range(start, n + 1))
