# Author: Kaustav Ghosh
# Problem: Delivering Boxes from Storage to Ports
# Approach: dp[i] = min trips for the first i boxes; one trip over [j, i) costs (port changes inside) + 2, so dp[i] = cumdiff[i] + 2 + min over the valid window of (dp[j] - cumdiff[j+1]), maintained with a monotonic deque

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
        weight = [0] * (n + 1)     # prefix weights
        cumdiff = [0] * (n + 1)    # prefix count of adjacent port changes
        for i in range(1, n + 1):
            weight[i] = weight[i - 1] + boxes[i - 1][1]
            change = 1 if i >= 2 and boxes[i - 1][0] != boxes[i - 2][0] else 0
            cumdiff[i] = cumdiff[i - 1] + change

        dp = [0] * (n + 1)
        dq = deque([0])  # candidate j's, increasing dp[j] - cumdiff[j+1]
        for i in range(1, n + 1):
            while dq and (i - dq[0] > maxBoxes or weight[i] - weight[dq[0]] > maxWeight):
                dq.popleft()
            j = dq[0]
            dp[i] = dp[j] - cumdiff[j + 1] + cumdiff[i] + 2
            if i < n:
                gi = dp[i] - cumdiff[i + 1]
                while dq and dp[dq[-1]] - cumdiff[dq[-1] + 1] >= gi:
                    dq.pop()
                dq.append(i)
        return dp[n]
