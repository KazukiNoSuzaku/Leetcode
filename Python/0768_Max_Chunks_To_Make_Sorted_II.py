# Find maximum chunks to sort an array with duplicates.

# Author: Kaustav Ghosh

class Solution(object):
    def maxChunksToSorted(self, arr):
        max_left = [0] * len(arr)
        min_right = [0] * len(arr)
        max_left[0] = arr[0]
        for i in range(1, len(arr)):
            max_left[i] = max(max_left[i-1], arr[i])
        min_right[-1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            min_right[i] = min(min_right[i+1], arr[i])
        return sum(max_left[i] <= min_right[i+1] for i in range(len(arr) - 1)) + 1
