class Solution:
    def maximumTastiness(self, price: list[int], k: int) -> int:
        # Binary search on tastiness; greedily pick k candies with consecutive gap >= mid.
        price.sort()

        def can_pick(t: int) -> bool:
            count, last = 1, price[0]
            for p in price[1:]:
                if p - last >= t:
                    count += 1
                    last = p
                    if count >= k:
                        return True
            return count >= k

        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_pick(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
