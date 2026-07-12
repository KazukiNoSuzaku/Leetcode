# Author: Kaustav Ghosh
# Problem: Maximum Number of Eaten Apples
# Approach: Each day add that day's batch with its expiry to a min-heap keyed by expiry; discard expired batches, then eat one apple from the soonest-to-rot batch

import heapq

class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        heap = []  # (expiry_day, count)
        eaten = 0
        day = 0
        n = len(apples)

        while day < n or heap:
            if day < n and apples[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))
            while heap and heap[0][0] <= day:  # rotten, drop
                heapq.heappop(heap)
            if heap:
                expiry, count = heapq.heappop(heap)
                eaten += 1
                if count - 1 > 0:
                    heapq.heappush(heap, (expiry, count - 1))
            day += 1

        return eaten
