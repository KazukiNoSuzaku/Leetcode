# Author: Kaustav Ghosh
# Problem: Minimum Number of Lines to Cover Points
# Approach: For each pair of points, precompute the set of points collinear with them. Recursively cover the first uncovered point by choosing a line through it (or a single-point line), minimizing the number of lines. Memoize on the covered bitmask

class Solution(object):
    def minimumLines(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return 1

        def collinear(a, b, c):
            return (points[b][0] - points[a][0]) * (points[c][1] - points[a][1]) == \
                   (points[b][1] - points[a][1]) * (points[c][0] - points[a][0])

        line_mask = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    mask = 0
                    for k in range(n):
                        if collinear(i, j, k):
                            mask |= 1 << k
                    line_mask[i][j] = mask

        full = (1 << n) - 1
        memo = {}

        def solve(covered):
            if covered == full:
                return 0
            if covered in memo:
                return memo[covered]
            i = 0
            while covered >> i & 1:
                i += 1
            best = 1 + solve(covered | (1 << i))  # single-point line
            for j in range(n):
                if j != i:
                    best = min(best, 1 + solve(covered | line_mask[i][j]))
            memo[covered] = best
            return best

        return solve(0)
