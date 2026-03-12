# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Huffman-like merging with split cost using min-heap

import heapq

class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """
        heapq.heapify(blocks)
        while len(blocks) > 1:
            a = heapq.heappop(blocks)
            b = heapq.heappop(blocks)
            heapq.heappush(blocks, b + split)
        return blocks[0]
