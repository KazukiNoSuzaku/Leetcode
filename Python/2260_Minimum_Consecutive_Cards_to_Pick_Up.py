# Author: Kaustav Ghosh
# Problem: Minimum Consecutive Cards to Pick Up
# Approach: The shortest run containing a matching pair spans from one occurrence of a value to its next occurrence. Track the last index of each value and, whenever a value repeats, update the answer with the distance between the two indices plus one. Return -1 if no value repeats

class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        last = {}
        best = float('inf')
        for i, c in enumerate(cards):
            if c in last:
                best = min(best, i - last[c] + 1)
            last[c] = i
        return best if best != float('inf') else -1
