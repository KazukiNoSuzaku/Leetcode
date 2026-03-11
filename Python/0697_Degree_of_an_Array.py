# Find the shortest subarray with the same degree (most frequent element count) as the array.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def findShortestSubArray(self, nums):
        count, first, last = {}, {}, {}
        for i, n in enumerate(nums):
            count[n] = count.get(n, 0) + 1
            if n not in first: first[n] = i
            last[n] = i
        degree = max(count.values())
        return min(last[n] - first[n] + 1 for n in count if count[n] == degree)
