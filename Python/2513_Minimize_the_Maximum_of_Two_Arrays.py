from math import gcd

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # Binary search on the answer m; use inclusion-exclusion over divisibility to verify.
        lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)

        def feasible(m: int) -> bool:
            excl1 = m // divisor2 - m // lcm   # usable only by arr1
            excl2 = m // divisor1 - m // lcm   # usable only by arr2
            shared = m - m // divisor1 - m // divisor2 + m // lcm
            need1 = max(0, uniqueCnt1 - excl1)  # must draw from shared pool
            need2 = max(0, uniqueCnt2 - excl2)
            return need1 + need2 <= shared

        lo, hi = 1, 2 * (uniqueCnt1 + uniqueCnt2)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
