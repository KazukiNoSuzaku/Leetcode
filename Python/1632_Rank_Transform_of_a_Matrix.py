# Author: Kaustav Ghosh
# https://leetcode.com/problems/rank-transform-of-a-matrix/

class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        m, n = len(matrix), len(matrix[0])

        # Group cells by value
        val_to_cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                val_to_cells[matrix[i][j]].append((i, j))

        rank = [[0] * n for _ in range(m)]
        row_max = [0] * m
        col_max = [0] * n

        for val in sorted(val_to_cells.keys()):
            cells = val_to_cells[val]
            # Union-Find for cells in same row/col with same value
            parent = {}
            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            def union(a, b):
                pa, pb = find(a), find(b)
                if pa != pb:
                    parent[pa] = pb

            row_groups = defaultdict(list)
            col_groups = defaultdict(list)
            for i, j in cells:
                parent[(i, j)] = (i, j)
                row_groups[i].append((i, j))
                col_groups[j].append((i, j))

            for group in list(row_groups.values()) + list(col_groups.values()):
                for k in range(1, len(group)):
                    union(group[0], group[k])

            # Group by root
            groups = defaultdict(list)
            for i, j in cells:
                groups[find((i, j))].append((i, j))

            for group in groups.values():
                max_rank = 0
                for i, j in group:
                    max_rank = max(max_rank, row_max[i], col_max[j])
                new_rank = max_rank + 1
                for i, j in group:
                    rank[i][j] = new_rank
                    row_max[i] = new_rank
                    col_max[j] = new_rank

        return rank
