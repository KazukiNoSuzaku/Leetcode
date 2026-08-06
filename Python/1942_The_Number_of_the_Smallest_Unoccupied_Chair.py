# Author: Kaustav Ghosh
# Problem: The Number of the Smallest Unoccupied Chair
# Approach: Process friends in arrival order. Before each arrival, free every chair whose occupant has already left (leaving time <= this arrival). Assign the smallest free chair from a min-heap; return it when the target friend is seated

import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        n = len(times)
        target_arrival = times[targetFriend][0]
        order = sorted(range(n), key=lambda i: times[i][0])

        free = list(range(n))
        heapq.heapify(free)
        occupied = []  # (leaving_time, chair)

        for i in order:
            arrive, leave = times[i]
            while occupied and occupied[0][0] <= arrive:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(free, chair)
            chair = heapq.heappop(free)
            if arrive == target_arrival:      # arrival times are unique
                return chair
            heapq.heappush(occupied, (leave, chair))
        return -1
