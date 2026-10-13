# Author: Kaustav Ghosh
# Problem: Sum of All Odd Length Subarrays
# Approach: Instead of generating the subarrays, I count how often each element is included: a subarray covering index i is fixed by choosing its start among the i+1 positions at or before i and its end among the n-i positions at or after i, giving (i+1)(n-i) subarrays in total, of which the odd-length ones are half, rounded up. Multiplying each element by that count gives the answer in a single pass.

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        total = 0
        for i, value in enumerate(arr):
            total += value * (((i + 1) * (n - i) + 1) // 2)
        return total
