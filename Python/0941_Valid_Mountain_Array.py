# Check if an array is a valid mountain (strictly increases then decreases).

# Author: Kaustav Ghosh

class Solution(object):
    def validMountainArray(self, arr):
        n = len(arr)
        i = 0
        while i < n-1 and arr[i] < arr[i+1]: i += 1
        if i == 0 or i == n-1: return False
        while i < n-1 and arr[i] > arr[i+1]: i += 1
        return i == n-1
