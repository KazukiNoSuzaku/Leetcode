# Grid of lamps; lamp illuminates its row, column, and both diagonals.
# For each query point, check if illuminated then turn off lamp and neighbors.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        row = defaultdict(int)
        col = defaultdict(int)
        diag = defaultdict(int)
        anti = defaultdict(int)
        lamp_set = set()
        for r, c in lamps:
            if (r, c) not in lamp_set:
                lamp_set.add((r, c))
                row[r] += 1
                col[c] += 1
                diag[r - c] += 1
                anti[r + c] += 1
        res = []
        for qr, qc in queries:
            if row[qr] or col[qc] or diag[qr - qc] or anti[qr + qc]:
                res.append(1)
            else:
                res.append(0)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = qr + dr, qc + dc
                    if (nr, nc) in lamp_set:
                        lamp_set.remove((nr, nc))
                        row[nr] -= 1
                        col[nc] -= 1
                        diag[nr - nc] -= 1
                        anti[nr + nc] -= 1
        return res
