import math

class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        lo, hi = 1, min(ranks) * cars * cars

        def can_repair(t):
            return sum(int(math.isqrt(t // r)) for r in ranks) >= cars

        while lo < hi:
            mid = (lo + hi) // 2
            if can_repair(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
