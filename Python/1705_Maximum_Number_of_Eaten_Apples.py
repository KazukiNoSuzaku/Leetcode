# Author: Kaustav Ghosh
# Problem: Maximum Number of Eaten Apples
# Approach: Only one apple may be eaten per day, so the question is which to choose, and the answer is always the batch that will spoil soonest: saving it gains nothing, while saving a longer-lived batch costs nothing. A min-heap keyed on the day a batch goes bad therefore makes the choice directly. Each day's new batch is added, anything already past its expiry is discarded from the front, and one apple is taken from whatever remains. The loop has to continue past the end of the harvest while any batch is still edible, since apples picked late may outlive the list.

from heapq import heappush, heappop


class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        batches = []
        eaten = 0
        day = 0
        n = len(apples)
        while day < n or batches:
            if day < n and apples[day] > 0:
                heappush(batches, (day + days[day], apples[day]))
            while batches and batches[0][0] <= day:
                heappop(batches)
            if batches:
                spoils, count = heappop(batches)
                eaten += 1
                if count > 1:
                    heappush(batches, (spoils, count - 1))
            day += 1
        return eaten
