from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x ascending, then y descending so we sweep left-to-right, high-to-low
        points.sort(key=lambda p: (p[0], -p[1]))
        n = ans = 0
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            max_y_between = float('-inf')  # max y of interior points with y <= yi
            for j in range(i + 1, n):
                xj, yj = points[j]
                if yi >= yj:  # valid upper-left / lower-right orientation
                    # blocked if any k in (i..j) had yj <= y[k] <= yi
                    if max_y_between < yj:
                        ans += 1
                # update: j becomes interior for future (i, j') with j' > j
                if yj <= yi:
                    max_y_between = max(max_y_between, yj)
        return ans
