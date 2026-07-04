# Author: Kaustav Ghosh
# Problem: Find Servers That Handled Most Number of Requests
# Approach: A busy min-heap frees servers by end time; a sorted set of free ids lets us pick the next id >= i%k (wrapping), then report the busiest

import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        free = SortedList(range(k))
        busy = []  # (end_time, server_id)
        count = [0] * k

        for i, start in enumerate(arrival):
            while busy and busy[0][0] <= start:
                _, sid = heapq.heappop(busy)
                free.add(sid)
            if not free:
                continue
            idx = free.bisect_left(i % k)
            if idx == len(free):
                idx = 0  # wrap around to the smallest available id
            sid = free[idx]
            free.remove(sid)
            count[sid] += 1
            heapq.heappush(busy, (start + load[i], sid))

        top = max(count)
        return [i for i in range(k) if count[i] == top]
