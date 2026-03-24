# Author: Kaustav Ghosh
# https://leetcode.com/problems/process-tasks-using-servers/

import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        # (weight, index) for free servers
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        # (end_time, index) for busy servers
        busy = []
        ans = []
        for t in range(len(tasks)):
            # Release servers that are done by time t
            while busy and busy[0][0] <= t:
                end, idx = heapq.heappop(busy)
                heapq.heappush(free, (servers[idx], idx))
            if free:
                w, idx = heapq.heappop(free)
                ans.append(idx)
                heapq.heappush(busy, (t + tasks[t], idx))
            else:
                # Wait for the earliest server to become free
                end, idx = heapq.heappop(busy)
                heapq.heappush(free, (servers[idx], idx))
                # Release all servers finishing at the same time
                while busy and busy[0][0] == end:
                    e2, i2 = heapq.heappop(busy)
                    heapq.heappush(free, (servers[i2], i2))
                w, idx2 = heapq.heappop(free)
                ans.append(idx2)
                heapq.heappush(busy, (end + tasks[t], idx2))
        return ans
