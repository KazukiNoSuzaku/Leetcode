# Author: Kaustav Ghosh
# Problem: Kth Missing Positive Number
# Approach: The array is sorted and strictly increasing, so the count of missing positives before arr[i] is arr[i] - i - 1, which only grows. Binary search for the first index where that count reaches k; everything before it is present, so the answer is that index plus k

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] - mid - 1 < k:
                low = mid + 1
            else:
                high = mid
        return low + k
