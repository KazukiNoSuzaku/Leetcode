# Author: Kaustav Ghosh
# Problem: Find Servers That Handled Most Number of Requests
# Approach: Each request wants the lowest-numbered free server at or after index i % k, falling back to the lowest free server overall, which is a "successor query" that a single heap cannot answer. The saving observation is that the preferred index advances by exactly one per request, so I split the free servers across two heaps, one holding the indices at or above the preferred index and one holding those below it. The answer is then the top of the first heap, or of the second when the first is empty. Advancing the preferred index can only strand the single index that just fell below it, and that index is necessarily sitting at the top of the first heap, so it is moved in one step; when the index wraps to zero the second heap is folded back in wholesale, which costs a full merge only once every k requests. A third heap keeps the busy servers ordered by the time they come free.

from heapq import heapify, heappush, heappop


class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        at_or_after = list(range(k))   # free servers with index >= preferred
        heapify(at_or_after)
        before = []                    # free servers with index < preferred
        busy = []                      # (time it frees up, server index)
        handled = [0] * k

        for i, start in enumerate(arrival):
            preferred = i % k
            if preferred == 0:
                if before:
                    for server in before:
                        heappush(at_or_after, server)
                    before = []
            elif at_or_after and at_or_after[0] == preferred - 1:
                # The index just overtaken is the only one that can be stranded.
                heappush(before, heappop(at_or_after))

            while busy and busy[0][0] <= start:
                _, server = heappop(busy)
                if server >= preferred:
                    heappush(at_or_after, server)
                else:
                    heappush(before, server)

            if at_or_after:
                server = heappop(at_or_after)
            elif before:
                server = heappop(before)
            else:
                continue               # every server busy, request dropped

            handled[server] += 1
            heappush(busy, (start + load[i], server))

        most = max(handled)
        return [server for server in range(k) if handled[server] == most]
