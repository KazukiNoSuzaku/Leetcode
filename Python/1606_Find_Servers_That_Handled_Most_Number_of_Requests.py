# Author: Kaustav Ghosh
# Problem: 1606 - Find Servers That Handled Most Number of Requests
# Approach: Sorted set for available servers + heap for busy servers

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
        count = [0] * k
        available = SortedList(range(k))
        busy = []  # (end_time, server_id)

        for i, (start, duration) in enumerate(zip(arrival, load)):
            # Free up servers
            while busy and busy[0][0] <= start:
                end, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            # Find server index >= i % k
            idx = available.bisect_left(i % k)
            if idx == len(available):
                idx = 0
            server = available[idx]
            available.remove(server)
            count[server] += 1
            heapq.heappush(busy, (start + duration, server))

        max_count = max(count)
        return [i for i in range(k) if count[i] == max_count]
