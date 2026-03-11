# Find cheapest flight from src to dst with at most k stops.

# Author: Kaustav Ghosh

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices[:]
            for u, v, w in flights:
                if prices[u] + w < temp[v]:
                    temp[v] = prices[u] + w
            prices = temp
        return prices[dst] if prices[dst] < float('inf') else -1
