# Author: Kaustav Ghosh
# Problem: Minimum Cost to Reach Destination in Time
# Approach: Cost and time pull against each other, so neither alone orders the states; the state has to be the pair of city and time used, and the quantity minimised is the fee for reaching that city having spent exactly that long. Because every edge consumes at least one minute, the times only ever increase, which means the table can be filled by sweeping the elapsed time upwards and relaxing every edge once per minute, with no priority queue needed. The answer is the cheapest fee recorded for the last city at any time within the budget.

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        n = len(passingFees)
        INF = float("inf")
        best = [[INF] * n for _ in range(maxTime + 1)]
        best[0][0] = passingFees[0]

        for spent in range(1, maxTime + 1):
            row = best[spent]
            for x, y, cost in edges:
                if cost > spent:
                    continue
                earlier = best[spent - cost]
                through = earlier[x]
                if through < INF and through + passingFees[y] < row[y]:
                    row[y] = through + passingFees[y]
                through = earlier[y]
                if through < INF and through + passingFees[x] < row[x]:
                    row[x] = through + passingFees[x]

        answer = min(best[spent][n - 1] for spent in range(maxTime + 1))
        return -1 if answer == INF else answer
