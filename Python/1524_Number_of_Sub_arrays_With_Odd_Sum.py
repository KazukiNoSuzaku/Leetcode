# Author: Kaustav Ghosh
# Problem: Number of Sub-arrays With Odd Sum
# Approach: Track prefix sum parity; odd-sum subarray needs prefix[l] and prefix[r] to differ in parity

class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        odd = even = ans = prefix = 0
        for x in arr:
            prefix += x
            if prefix % 2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1
        return ans % MOD
