from bisect import bisect_right

class Solution:
    def minimumTime(self, hens: list[int], grains: list[int]) -> int:
        hens.sort()
        grains.sort()
        m = len(grains)

        def can_eat(T):
            j = 0
            for h in hens:
                if j == m:
                    return True
                L = max(0, h - grains[j])
                if L > T:
                    return False
                # Go left-first: r <= T - 2L  OR  go right-first: r <= (T-L)//2
                max_right = h + max(T - 2 * L, (T - L) // 2)
                j = bisect_right(grains, max_right, j)
            return j >= m

        lo, hi = 0, 2 * 10 ** 9
        while lo < hi:
            mid = (lo + hi) // 2
            if can_eat(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
