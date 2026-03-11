# The median is the middle value in an ordered integer list.
# Given an array of integers nums and an integer k, there is a sliding window of size k
# which is moving from the very left to the right. Return the median array for each window.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        lo = []  # max-heap (negated)
        hi = []  # min-heap
        lazy = {}  # elements to be removed

        def add(x):
            if lo and x <= -lo[0]:
                heapq.heappush(lo, -x)
            else:
                heapq.heappush(hi, x)
            rebalance()

        def remove(x):
            lazy[x] = lazy.get(x, 0) + 1
            if x <= -lo[0]:
                clean_lo()
            else:
                clean_hi()
            rebalance()

        def clean_lo():
            while lo and lazy.get(-lo[0], 0):
                lazy[-lo[0]] -= 1
                heapq.heappop(lo)

        def clean_hi():
            while hi and lazy.get(hi[0], 0):
                lazy[hi[0]] -= 1
                heapq.heappop(hi)

        def rebalance():
            while len(lo) > len(hi) + 1:
                heapq.heappush(hi, -heapq.heappop(lo))
                clean_lo(); clean_hi()
            while len(hi) > len(lo):
                heapq.heappush(lo, -heapq.heappop(hi))
                clean_lo(); clean_hi()

        def median():
            if k % 2 == 1:
                return float(-lo[0])
            return (-lo[0] + hi[0]) / 2.0

        for i in range(k):
            add(nums[i])
        res = [median()]
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            clean_lo(); clean_hi()
            res.append(median())
        return res
