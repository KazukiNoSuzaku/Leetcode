class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        # Large range: sort banned, greedily take consecutive runs of allowed integers in O(|banned|) segments.
        banned_sorted = sorted(set(x for x in banned if 1 <= x <= n))
        count = total = 0
        prev = 0
        for b in banned_sorted + [n + 1]:
            lo, hi = prev + 1, b - 1
            if lo <= hi:
                remaining = maxSum - total
                if remaining <= 0:
                    break
                # Take first k integers lo..lo+k-1 with sum k*lo + k*(k-1)//2 <= remaining
                k_lo, k_hi = 0, hi - lo + 1
                while k_lo < k_hi:
                    mid = (k_lo + k_hi + 1) // 2
                    if mid * lo + mid * (mid - 1) // 2 <= remaining:
                        k_lo = mid
                    else:
                        k_hi = mid - 1
                count += k_lo
                total += k_lo * lo + k_lo * (k_lo - 1) // 2
                if k_lo < hi - lo + 1:
                    break
            prev = b
        return count
