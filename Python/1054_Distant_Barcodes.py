# Author: Kaustav Ghosh
# 1054. Distant Barcodes
# https://leetcode.com/problems/distant-barcodes/

import heapq
from collections import Counter

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        count = Counter(barcodes)
        heap = [(-freq, val) for val, freq in count.items()]
        heapq.heapify(heap)
        result = []
        while heap:
            freq1, val1 = heapq.heappop(heap)
            if not result or result[-1] != val1:
                result.append(val1)
                if freq1 + 1 < 0:
                    heapq.heappush(heap, (freq1 + 1, val1))
            else:
                if not heap:
                    break
                freq2, val2 = heapq.heappop(heap)
                result.append(val2)
                if freq2 + 1 < 0:
                    heapq.heappush(heap, (freq2 + 1, val2))
                heapq.heappush(heap, (freq1, val1))
        return result
