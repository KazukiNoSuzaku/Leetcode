# Author: Kaustav Ghosh
# 2204. Distance to a Cycle in Undirected Graph
# https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/
# Difficulty: Hard (Premium)
#
# Approach (Premium - solution in comments):
# 1. Find all nodes on a cycle by repeatedly removing leaf nodes (degree-1 nodes),
#    similar to topological peel. Remaining nodes form the cycle(s).
# 2. BFS outward from all cycle nodes simultaneously (multi-source BFS).
#    The BFS distance from the nearest cycle node is the answer for each node.
#
# from collections import deque
#
# class Solution(object):
#     def distanceToCycle(self, n, edges):
#         adj = [set() for _ in range(n)]
#         for u, v in edges:
#             adj[u].add(v)
#             adj[v].add(u)
#         degree = [len(adj[i]) for i in range(n)]
#         queue = deque(i for i in range(n) if degree[i] == 1)
#         removed = set()
#         while queue:
#             node = queue.popleft()
#             removed.add(node)
#             for nb in adj[node]:
#                 if nb not in removed:
#                     degree[nb] -= 1
#                     if degree[nb] == 1:
#                         queue.append(nb)
#         # Remaining nodes (not removed) are on the cycle
#         on_cycle = set(range(n)) - removed
#         # Multi-source BFS from all cycle nodes
#         dist = [-1] * n
#         bfs = deque()
#         for node in on_cycle:
#             dist[node] = 0
#             bfs.append(node)
#         while bfs:
#             node = bfs.popleft()
#             for nb in adj[node]:
#                 if dist[nb] == -1:
#                     dist[nb] = dist[node] + 1
#                     bfs.append(nb)
#         return dist

class Solution(object):
    pass
