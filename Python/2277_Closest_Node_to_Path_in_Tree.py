# Author: Kaustav Ghosh
# Problem: 2277. Closest Node to Path in Tree
# URL: https://leetcode.com/problems/closest-node-to-path-in-tree/
# Difficulty: Hard
# Premium: True
#
# Approach:
# For each query (start, end, node): find the path from start to end using LCA,
# then for each node on that path compute the distance to the query node.
# The closest node on the path is the answer.
#
# Optimized: For query node, find its LCA with start and end. The closest
# point on path(start, end) to node is determined by LCA relationships.
#
# def closestNode(n, edges, query):
#     from collections import defaultdict, deque
#     adj = defaultdict(list)
#     for u, v in edges:
#         adj[u].append(v)
#         adj[v].append(u)
#     # BFS to find parent and depth arrays for LCA
#     LOG = 17
#     parent = [[-1]*n for _ in range(LOG)]
#     depth = [0]*n
#     visited = [False]*n
#     q = deque([0])
#     visited[0] = True
#     while q:
#         u = q.popleft()
#         for v in adj[u]:
#             if not visited[v]:
#                 visited[v] = True
#                 parent[0][v] = u
#                 depth[v] = depth[u]+1
#                 q.append(v)
#     for k in range(1, LOG):
#         for v in range(n):
#             if parent[k-1][v] != -1:
#                 parent[k][v] = parent[k-1][parent[k-1][v]]
#     def lca(u, v):
#         if depth[u] < depth[v]: u, v = v, u
#         diff = depth[u] - depth[v]
#         for k in range(LOG):
#             if (diff >> k) & 1: u = parent[k][u]
#         if u == v: return u
#         for k in range(LOG-1, -1, -1):
#             if parent[k][u] != parent[k][v]:
#                 u = parent[k][u]
#                 v = parent[k][v]
#         return parent[0][u]
#     def dist(u, v):
#         return depth[u] + depth[v] - 2*depth[lca(u, v)]
#     result = []
#     for s, e, nd in query:
#         l = lca(s, e)
#         # Candidates: lca(s, nd) if on path, lca(e, nd) if on path, l
#         candidates = set()
#         for c in [lca(s, nd), lca(e, nd), l]:
#             if dist(s, c) + dist(c, e) == dist(s, e):
#                 candidates.add(c)
#         best = min(candidates, key=lambda c: dist(c, nd))
#         result.append(best)
#     return result

class Solution(object):
    pass
