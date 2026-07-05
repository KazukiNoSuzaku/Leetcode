# Author: Kaustav Ghosh
# Problem: Rank Transform of a Matrix
# Approach: Process values ascending; union equal cells sharing a row/col, then each group's rank is 1 + the largest rank already used in any of its rows or columns

from collections import defaultdict

class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(matrix), len(matrix[0])
        by_value = defaultdict(list)
        for i in range(R):
            for j in range(C):
                by_value[matrix[i][j]].append((i, j))

        rank = [[0] * C for _ in range(R)]
        row_rank = [0] * R
        col_rank = [0] * C

        for val in sorted(by_value):
            parent = {}

            def find(x):
                parent.setdefault(x, x)
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(a, b):
                parent[find(a)] = find(b)

            # Cells of equal value in the same row/col must share a rank
            for i, j in by_value[val]:
                union(('row', i), ('col', j))

            groups = defaultdict(list)
            for i, j in by_value[val]:
                groups[find(('row', i))].append((i, j))

            for cells in groups.values():
                best = 1
                for i, j in cells:
                    best = max(best, row_rank[i] + 1, col_rank[j] + 1)
                for i, j in cells:
                    rank[i][j] = best
                    row_rank[i] = best
                    col_rank[j] = best

        return rank
