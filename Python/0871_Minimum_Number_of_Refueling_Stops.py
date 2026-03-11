# Find minimum refueling stops to reach target given fuel and station list.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        heap = []
        fuel = startFuel
        stops = 0
        prev = 0
        for loc, cap in stations + [(target, 0)]:
            fuel -= loc - prev
            while fuel < 0 and heap:
                fuel -= heapq.heappop(heap)
                stops += 1
            if fuel < 0: return -1
            heapq.heappush(heap, -cap)
            prev = loc
        return stops
