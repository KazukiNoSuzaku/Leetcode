# Find max chunks such that each chunk sorted gives the sorted array.

# Author: Kaustav Ghosh

class Solution(object):
    def maxChunksToSorted(self, arr):
        chunks = 0
        max_so_far = 0
        for i, x in enumerate(arr):
            max_so_far = max(max_so_far, x)
            if max_so_far == i:
                chunks += 1
        return chunks
