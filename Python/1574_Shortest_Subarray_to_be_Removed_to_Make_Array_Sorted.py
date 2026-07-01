# Author: Kaustav Ghosh
# Problem: Shortest Subarray to be Removed to Make Array Sorted
# Approach: Keep the longest sorted prefix and suffix, then two-pointer-merge them to find the largest overlap we can bridge

class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0

        right = n - 1
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Remove everything after the prefix, or everything before the suffix
        best = min(n - left - 1, right)

        i, j = 0, right
        while i <= left and j < n:
            if arr[j] >= arr[i]:
                best = min(best, j - i - 1)
                i += 1
            else:
                j += 1
        return best
