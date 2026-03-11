# Find shortest subarray with sum >= k (can have negatives).

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n): prefix[i+1] = prefix[i] + nums[i]
        res = n + 1
        dq = deque()
        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                res = min(res, i - dq.popleft())
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)
        return res if res <= n else -1
