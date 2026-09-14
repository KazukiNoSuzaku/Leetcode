# Author: Kaustav Ghosh
# Problem: Design a Number Container System
# Approach: Store the current number at each index, and for each number a min-heap of indices that have held it. change records the new number and pushes the index onto that number's heap; find lazily pops indices whose current number no longer matches, leaving the smallest valid index on top

import heapq
from collections import defaultdict


class NumberContainers(object):

    def __init__(self):
        self.at = {}
        self.heaps = defaultdict(list)

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        self.at[index] = number
        heapq.heappush(self.heaps[number], index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        heap = self.heaps.get(number)
        while heap and self.at[heap[0]] != number:
            heapq.heappop(heap)
        return heap[0] if heap else -1
