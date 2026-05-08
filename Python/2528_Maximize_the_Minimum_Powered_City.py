from itertools import accumulate

class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        # Binary search on min power; greedily place needed stations at rightmost reachable position.
        n = len(stations)
        prefix = list(accumulate(stations, initial=0))
        power = [prefix[min(n, i + r + 1)] - prefix[max(0, i - r)] for i in range(n)]

        def feasible(m: int) -> bool:
            diff = [0] * (n + 1)
            added = extra = 0
            for i in range(n):
                extra += diff[i]
                deficit = m - power[i] - extra
                if deficit > 0:
                    added += deficit
                    if added > k:
                        return False
                    extra += deficit
                    if i + 2 * r + 1 <= n:
                        diff[i + 2 * r + 1] -= deficit
            return True

        lo, hi = min(power), min(power) + k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
