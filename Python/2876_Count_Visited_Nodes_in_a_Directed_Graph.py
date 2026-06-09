from typing import List

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        res = [0] * n
        color = [0] * n  # 0: unvisited, 1: in current path, 2: resolved

        for i in range(n):
            if color[i] != 0:
                continue
            path = []
            node = i
            while color[node] == 0:
                color[node] = 1
                path.append(node)
                node = edges[node]

            if color[node] == 1:
                # Found a new cycle; locate where it starts in path
                idx = 0
                while path[idx] != node:
                    idx += 1
                cycle_len = len(path) - idx
                for j in range(idx, len(path)):
                    res[path[j]] = cycle_len
                    color[path[j]] = 2
                for j in range(idx - 1, -1, -1):
                    res[path[j]] = res[path[j + 1]] + 1
                    color[path[j]] = 2
            else:
                # Tail leading into an already-resolved node
                for j in range(len(path) - 1, -1, -1):
                    res[path[j]] = res[edges[path[j]]] + 1
                    color[path[j]] = 2

        return res
