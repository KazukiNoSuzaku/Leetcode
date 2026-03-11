# Find k-th smallest prime fraction p/q from a sorted array of primes.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        heap = [(arr[0] / float(arr[j]), 0, j) for j in range(1, n)]
        heapq.heapify(heap)
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap, (arr[i+1] / float(arr[j]), i+1, j))
        _, i, j = heap[0]
        return [arr[i], arr[j]]
