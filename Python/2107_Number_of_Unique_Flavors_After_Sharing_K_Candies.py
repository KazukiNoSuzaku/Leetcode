# Author: Kaustav Ghosh
# Problem: Number of Unique Flavors After Sharing K Candies
# Approach: You give away a contiguous window of exactly k candies and keep the rest. Slide that window; maintain a counter of the kept candies and a running count of distinct flavors still present, updating as one candy enters the window and another leaves it

from collections import Counter

class Solution(object):
    def shareCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return len(set(candies))

        n = len(candies)
        remaining = Counter(candies)
        distinct = len(remaining)
        for x in candies[:k]:
            remaining[x] -= 1
            if remaining[x] == 0:
                distinct -= 1

        best = distinct
        for i in range(k, n):
            remaining[candies[i]] -= 1
            if remaining[candies[i]] == 0:
                distinct -= 1
            if remaining[candies[i - k]] == 0:
                distinct += 1
            remaining[candies[i - k]] += 1
            best = max(best, distinct)
        return best
