# Author: Kaustav Ghosh
# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

from collections import deque

class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        n = len(boxes)
        # trips[i] = number of port changes from box i to box i+1
        trips = [0] * n
        for i in range(1, n):
            trips[i] = trips[i - 1] + (1 if boxes[i][0] != boxes[i - 1][0] else 0)

        dp = [0] * (n + 1)
        weight_sum = 0
        dq = deque([0])

        j = 0
        for i in range(1, n + 1):
            weight_sum += boxes[i - 1][1]
            while i - j > maxBoxes or weight_sum > maxWeight:
                j += 1
                weight_sum -= boxes[j - 1][1]
            while dq and dq[0] < j:
                dq.popleft()
            dp[i] = dp[dq[0]] + trips[i - 1] - trips[dq[0]] + 2
            if i < n:
                while dq and dp[dq[-1]] - trips[dq[-1]] >= dp[i] - trips[i]:
                    dq.pop()
                dq.append(i)
        return dp[n]
