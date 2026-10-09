# Author: Kaustav Ghosh
# Problem: Most Visited Sector in a Circular Track
# Approach: Every full lap visits each sector equally, so only the leftover stretch from the first sector to the last one decides the winners. That stretch is the plain range when it does not wrap, and the two end pieces of the track when it does

class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        start, finish = rounds[0], rounds[-1]
        if start <= finish:
            return list(range(start, finish + 1))
        return list(range(1, finish + 1)) + list(range(start, n + 1))
