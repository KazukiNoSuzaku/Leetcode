# Author: Kaustav Ghosh
# Problem: Painting a Grid With Three Different Colors
# Approach: A column is m cells; there are few valid single-column colorings (no vertical repeats). Precompute them and which pairs are compatible as neighbors (no same color in any row), then run a column-by-column DP counting colorings across the n columns

class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        # all valid colorings of one column (no two vertically adjacent equal)
        states = []
        def build(col):
            if len(col) == m:
                states.append(tuple(col))
                return
            for c in range(3):
                if not col or col[-1] != c:
                    col.append(c)
                    build(col)
                    col.pop()
        build([])

        # compatibility between adjacent columns
        compat = {s: [] for s in states}
        for a in states:
            for b in states:
                if all(a[i] != b[i] for i in range(m)):
                    compat[a].append(b)

        dp = {s: 1 for s in states}
        for _ in range(n - 1):
            ndp = {s: 0 for s in states}
            for s, cnt in dp.items():
                if cnt:
                    for t in compat[s]:
                        ndp[t] = (ndp[t] + cnt) % MOD
            dp = ndp

        return sum(dp.values()) % MOD
