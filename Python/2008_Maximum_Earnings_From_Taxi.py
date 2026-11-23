# Author: Kaustav Ghosh
# Problem: Maximum Earnings From Taxi
# Approach: The taxi only ever moves forward, so the best earnings achievable by the time it reaches a point depend solely on that point, which makes a sweep along the road from the first point to the last enough. At each point the driver either rolls past it unchanged, keeping the best total from the point before, or finishes a ride that ends exactly there, in which case the total is the best achievable at that ride's start plus the distance covered and the tip. Bucketing the rides by their end point means every ride is considered once, so the sweep costs the length of the road plus the number of rides.

class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        ending = [[] for _ in range(n + 1)]
        for start, end, tip in rides:
            ending[end].append((start, end - start + tip))
        best = [0] * (n + 1)
        for point in range(1, n + 1):
            carried = best[point - 1]
            for start, payment in ending[point]:
                candidate = best[start] + payment
                if candidate > carried:
                    carried = candidate
            best[point] = carried
        return best[n]
