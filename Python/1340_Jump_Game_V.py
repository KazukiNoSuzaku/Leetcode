# From index i, jump to j if |i-j| <= d and arr[j] < arr[i] (no taller in between).
# Return maximum number of indices reachable.

# Author: Kaustav Ghosh

class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        memo = {}
        def dp(i):
            if i in memo: return memo[i]
            best = 1
            for di in [1, -1]:
                for step in range(1, d + 1):
                    j = i + di * step
                    if not (0 <= j < n): break
                    if arr[j] >= arr[i]: break
                    best = max(best, 1 + dp(j))
            memo[i] = best
            return best
        return max(dp(i) for i in range(n))
