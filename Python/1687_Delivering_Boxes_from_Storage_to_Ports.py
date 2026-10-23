# Author: Kaustav Ghosh
# Problem: Delivering Boxes from Storage to Ports
# Approach: Boxes must be shipped in order, so a plan is just a cut of the sequence into consecutive loads, and the cost of one load is two trips for leaving and returning plus one extra leg for every point inside the load where the destination port changes. Writing those port changes as a prefix count makes a load's cost depend on its endpoints alone, and the recurrence for the best cost up to a point becomes a minimum of the earlier best minus its prefix count, taken over the loads that fit. Both constraints bound the load from the same side, since the capacity and the weight limit are each violated only by starting too far back, so the candidate starts form a sliding window and a monotonic deque keeps the minimum over it; every box enters and leaves the deque once, making the whole thing linear.

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
        weight = [0] * (n + 1)
        changes = [0] * n
        for t in range(n):
            weight[t + 1] = weight[t] + boxes[t][1]
            if t:
                changes[t] = changes[t - 1] + (1 if boxes[t][0] != boxes[t - 1][0] else 0)

        trips = [0] * (n + 1)
        window = deque()
        for i in range(1, n + 1):
            start = i - 1
            key = trips[start] - changes[start]
            while window and trips[window[-1]] - changes[window[-1]] >= key:
                window.pop()
            window.append(start)
            # A start too far back breaks either the count limit or the weight limit.
            while window[0] < i - maxBoxes or weight[i] - weight[window[0]] > maxWeight:
                window.popleft()
            front = window[0]
            trips[i] = trips[front] - changes[front] + changes[i - 1] + 2
        return trips[n]
