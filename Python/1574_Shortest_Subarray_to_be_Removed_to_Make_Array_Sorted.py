# Author: Kaustav Ghosh
# Problem: 1574 - Shortest Subarray to be Removed to Make Array Sorted
# Approach: Two pointers from sorted prefix and sorted suffix

class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        # find longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        # find longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # remove either prefix or suffix
        result = min(n - left - 1, right)

        # try keeping part of prefix and part of suffix
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result
