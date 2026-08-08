# Author: Kaustav Ghosh
# Problem: Minimum Time For K Virus Variants to Spread
# Approach: Manhattan distance becomes Chebyshev distance under the rotation u=x+y, v=x-y, so each variant covers an axis-aligned square of half-side t. Binary search t and test feasibility: does some integer lattice point (u,v) with u==v mod 2 (a real cell) lie inside at least k squares. Candidate coordinates are square edges (and +-1 for parity)

class Solution(object):
    def minDayskVariants(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        tp = [(x + y, x - y) for x, y in points]

        def feasible(t):
            u_candidates = set()
            for up, _ in tp:
                for edge in (up - t, up + t):
                    u_candidates.update((edge - 1, edge, edge + 1))
            for u in u_candidates:
                active = [(vp - t, vp + t) for up, vp in tp if up - t <= u <= up + t]
                if len(active) < k:
                    continue
                v_candidates = set()
                for lo, hi in active:
                    for base in (lo, hi):
                        v_candidates.update((base - 1, base, base + 1))
                for v in v_candidates:
                    if (v - u) % 2 != 0:      # need x, y integer
                        continue
                    cover = 0
                    for lo, hi in active:
                        if lo <= v <= hi:
                            cover += 1
                    if cover >= k:
                        return True
            return False

        us = [p[0] for p in tp]
        vs = [p[1] for p in tp]
        hi = max(max(us) - min(us), max(vs) - min(vs)) + 2
        lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
