# Author: Kaustav Ghosh
# Problem: 1588 - Sum of All Odd Length Subarrays
# Approach: Count how many odd-length subarrays include each index

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        result = 0
        for i in range(n):
            # subarrays containing arr[i]
            # left choices: i+1, right choices: n-i
            left = i + 1
            right = n - i
            # subarrays with odd length including i
            # = ceil(left/2)*ceil(right/2) + floor(left/2)*floor(right/2)
            result += arr[i] * ((left + 1) // 2 * (right + 1) // 2 + left // 2 * (right // 2))
        return result
