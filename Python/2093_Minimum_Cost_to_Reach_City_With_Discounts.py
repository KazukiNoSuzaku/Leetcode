# Author: Kaustav Ghosh
# Problem 2093: Minimum Cost to Reach City With Discounts
# Premium Problem
#
# There are n cities and m highways connecting them. Each highway has a toll.
# You can use up to 'discounts' number of discount coupons, each halving a toll.
# Find minimum cost to travel from city 0 to city n-1.
#
# Solution: Modified Dijkstra with state (city, discounts_remaining).
# Use priority queue tracking (cost, city, discounts_left).
# For each edge, consider paying full toll or using a discount (toll // 2).
#
# import heapq
#
# class Solution(object):
#     def minimumCost(self, n, highways, discounts):
#         """
#         :type n: int
#         :type highways: List[List[int]]
#         :type discounts: int
#         :rtype: int
#         """
#         graph = [[] for _ in range(n)]
#         for u, v, w in highways:
#             graph[u].append((v, w))
#             graph[v].append((u, w))
#         dist = [[float('inf')] * (discounts + 1) for _ in range(n)]
#         dist[0][discounts] = 0
#         pq = [(0, 0, discounts)]
#         while pq:
#             cost, u, d = heapq.heappop(pq)
#             if u == n - 1:
#                 return cost
#             if cost > dist[u][d]:
#                 continue
#             for v, w in graph[u]:
#                 # Without discount
#                 if cost + w < dist[v][d]:
#                     dist[v][d] = cost + w
#                     heapq.heappush(pq, (cost + w, v, d))
#                 # With discount
#                 if d > 0 and cost + w // 2 < dist[v][d - 1]:
#                     dist[v][d - 1] = cost + w // 2
#                     heapq.heappush(pq, (cost + w // 2, v, d - 1))
#         return -1

class Solution(object):
    pass
