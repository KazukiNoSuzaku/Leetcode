# Author: Kaustav Ghosh
# Problem: Shortest Subarray to be Removed to Make Array Sorted
# Approach: Whatever is removed is one middle block, so the survivors are a prefix of the already non-decreasing run at the front glued to a suffix of the non-decreasing run at the back. I find those two runs, consider the two extremes of dropping one side entirely, and then slide two pointers to find for each prefix end the earliest suffix start whose first value is at least as large: because both runs are sorted, that pointer only ever moves forward, so the best join is found in one linear sweep.

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
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        # Either keep only the prefix, or keep only the suffix.
        best = min(n - left - 1, right)
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                if j - i - 1 < best:
                    best = j - i - 1
                i += 1
            else:
                j += 1
        return best
