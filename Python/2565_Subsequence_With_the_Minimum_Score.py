class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        # Binary search per prefix: left[l] = s-index after greedily matching t[0..l-1] from left.
        # right[r] = s-index where t[r..m-1] starts when matched from right (non-decreasing).
        # For each l, find min p with right[p] > left[l]; score = p - l.
        n, m = len(s), len(t)
        left = [n] * (m + 1)
        left[0] = -1
        si = 0
        for l in range(1, m + 1):
            while si < n and s[si] != t[l - 1]:
                si += 1
            if si < n:
                left[l] = si
                si += 1

        right = [n] * (m + 1)
        si = n - 1
        for r in range(m - 1, -1, -1):
            while si >= 0 and s[si] != t[r]:
                si -= 1
            if si >= 0:
                right[r] = si
                si -= 1
            else:
                break

        ans = m
        for l in range(m + 1):
            if left[l] == n:
                break
            lo, hi = l, m
            while lo < hi:
                mid = (lo + hi) // 2
                if right[mid] > left[l]:
                    hi = mid
                else:
                    lo = mid + 1
            ans = min(ans, lo - l)
            if ans == 0:
                return 0
        return ans
