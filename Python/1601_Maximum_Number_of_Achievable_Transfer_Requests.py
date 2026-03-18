# Author: Kaustav Ghosh
# Problem: 1601 - Maximum Number of Achievable Transfer Requests
# Approach: Bitmask enumerate all subsets, check net flow is zero for all buildings

class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        m = len(requests)
        result = 0

        for mask in range(1 << m):
            net = [0] * n
            count = 0
            for i in range(m):
                if mask >> i & 1:
                    f, t = requests[i]
                    net[f] -= 1
                    net[t] += 1
                    count += 1
            if all(x == 0 for x in net):
                result = max(result, count)

        return result
