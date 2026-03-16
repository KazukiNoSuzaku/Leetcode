# Author: Kaustav Ghosh
# Problem: Longest Happy String
# Approach: Greedy max-heap, pick most frequent char not causing triple repeat

import heapq

class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        heap = []
        if a: heapq.heappush(heap, (-a, 'a'))
        if b: heapq.heappush(heap, (-b, 'b'))
        if c: heapq.heappush(heap, (-c, 'c'))
        result = []
        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == ch1:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                cnt2 += 1
                if cnt2:
                    heapq.heappush(heap, (cnt2, ch2))
                heapq.heappush(heap, (cnt1, ch1))
            else:
                result.append(ch1)
                cnt1 += 1
                if cnt1:
                    heapq.heappush(heap, (cnt1, ch1))
        return ''.join(result)
