# Author: Kaustav Ghosh
# Problem: Sum of All Odd Length Subarrays
# Approach: Count each element's contribution: with (i+1)*(n-i) subarrays covering it, half (rounded up) have odd length

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        total = 0
        for i, x in enumerate(arr):
            subarrays = (i + 1) * (n - i)
            odd = (subarrays + 1) // 2
            total += odd * x
        return total
