# Count subarrays of size k whose average >= threshold.

# Author: Kaustav Ghosh

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        target = threshold * k
        window = sum(arr[:k])
        res = 1 if window >= target else 0
        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            if window >= target:
                res += 1
        return res
