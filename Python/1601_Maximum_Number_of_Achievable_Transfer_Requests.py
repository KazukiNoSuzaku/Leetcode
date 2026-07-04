# Author: Kaustav Ghosh
# Problem: Maximum Number of Achievable Transfer Requests
# Approach: With at most 16 requests, try every subset via bitmask; a subset works only if every building's net in/out change is zero

class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        r = len(requests)
        best = 0
        for mask in range(1 << r):
            degree = [0] * n
            picked = 0
            for i in range(r):
                if mask >> i & 1:
                    frm, to = requests[i]
                    degree[frm] -= 1
                    degree[to] += 1
                    picked += 1
            if picked > best and all(d == 0 for d in degree):
                best = picked
        return best
