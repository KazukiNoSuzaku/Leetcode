# Return the k most frequent words sorted by frequency then lexicographically.

# Author: Kaustav Ghosh

from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
