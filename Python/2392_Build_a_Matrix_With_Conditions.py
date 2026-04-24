from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def topo_sort(conditions):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            q = deque(i for i in range(1, k + 1) if indegree[i] == 0)
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nb in graph[node]:
                    indegree[nb] -= 1
                    if indegree[nb] == 0:
                        q.append(nb)
            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        if not row_order or not col_order:
            return []
        row_pos = {v: i for i, v in enumerate(row_order)}
        col_pos = {v: i for i, v in enumerate(col_order)}
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        return matrix
