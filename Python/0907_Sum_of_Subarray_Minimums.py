# Find sum of minimums of all subarrays mod 10^9+7.

# Author: Kaustav Ghosh

class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        stack = []
        res = 0
        arr = [0] + arr + [0]
        for i, x in enumerate(arr):
            while stack and arr[stack[-1]] > x:
                mid = stack.pop()
                left = stack[-1]
                res = (res + arr[mid] * (mid - left) * (i - mid)) % MOD
            stack.append(i)
        return res
