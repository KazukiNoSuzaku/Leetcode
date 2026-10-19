# Author: Kaustav Ghosh
# Problem: Rank Transform of a Matrix
# Approach: Equal values sharing a row or a column must receive the same rank, and that constraint is transitive, so for each distinct value the cells it occupies have to be gathered into groups linked through shared rows and columns, which is what a union-find over row and column labels does. Values are then settled in ascending order, because a cell's rank depends only on what is already placed below it: a group's rank is one more than the highest rank yet assigned anywhere in any of its rows or columns, and that single rank is written to every cell of the group, after which those rows and columns record it as their new maximum. Treating the group as a unit is what keeps tied cells consistent without ever revisiting a decision.

from collections import defaultdict


class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        cells_by_value = defaultdict(list)
        for r in range(rows):
            row = matrix[r]
            for c in range(cols):
                cells_by_value[row[c]].append((r, c))

        row_best = [0] * rows
        col_best = [0] * cols
        answer = [[0] * cols for _ in range(rows)]

        for value in sorted(cells_by_value):
            cells = cells_by_value[value]
            parent = {}

            def find(x):
                if x not in parent:
                    parent[x] = x
                    return x
                root = x
                while parent[root] != root:
                    root = parent[root]
                while parent[x] != root:
                    parent[x], x = root, parent[x]
                return root

            # Link the row label and the column label of every cell of this value.
            for r, c in cells:
                a, b = find(r), find(~c)
                if a != b:
                    parent[a] = b

            groups = defaultdict(list)
            for r, c in cells:
                groups[find(r)].append((r, c))

            for group in groups.values():
                rank = 1
                for r, c in group:
                    if row_best[r] + 1 > rank:
                        rank = row_best[r] + 1
                    if col_best[c] + 1 > rank:
                        rank = col_best[c] + 1
                for r, c in group:
                    answer[r][c] = rank
                    row_best[r] = rank
                    col_best[c] = rank
        return answer
