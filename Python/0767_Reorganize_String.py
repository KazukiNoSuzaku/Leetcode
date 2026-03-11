# Rearrange string so no two adjacent characters are the same.

# Author: Kaustav Ghosh

import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        heap = [(-cnt, c) for c, cnt in Counter(s).items()]
        heapq.heapify(heap)
        res = []
        while len(heap) >= 2:
            c1, ch1 = heapq.heappop(heap)
            c2, ch2 = heapq.heappop(heap)
            res += [ch1, ch2]
            if c1 + 1: heapq.heappush(heap, (c1 + 1, ch1))
            if c2 + 1: heapq.heappush(heap, (c2 + 1, ch2))
        if heap:
            c, ch = heap[0]
            if -c > 1: return ''
            res.append(ch)
        return ''.join(res)
