# Author: Kaustav Ghosh
# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        events = []
        for i, (a, l) in enumerate(times):
            events.append((a, 0, i))  # arrive
            events.append((l, 1, i))  # leave
        events.sort()

        available = list(range(len(times)))
        heapq.heapify(available)
        assigned = {}

        for time, typ, idx in events:
            if typ == 1:  # leaving
                heapq.heappush(available, assigned[idx])
            else:  # arriving
                chair = heapq.heappop(available)
                assigned[idx] = chair
                if idx == targetFriend:
                    return chair
        return -1
