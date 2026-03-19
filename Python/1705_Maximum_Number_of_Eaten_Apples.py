# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-number-of-eaten-apples/

import heapq

class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        n = len(apples)
        heap = []  # (expiry_day, count)
        eaten = 0
        day = 0
        while day < n or heap:
            if day < n and apples[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))
            while heap and (heap[0][0] <= day or heap[0][1] == 0):
                heapq.heappop(heap)
            if heap:
                expiry, count = heapq.heappop(heap)
                eaten += 1
                if count - 1 > 0:
                    heapq.heappush(heap, (expiry, count - 1))
            day += 1
        return eaten
