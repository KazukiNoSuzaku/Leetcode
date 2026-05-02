class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        start = 0  # next palindrome must begin at >= start

        def try_center(lo, hi):
            nonlocal ans, start
            # Expand from center; take the shortest palindrome of length >= k starting at >= start
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                if hi - lo + 1 >= k and lo >= start:
                    ans += 1
                    start = hi + 1
                    return
                lo -= 1
                hi += 1

        for i in range(n):
            try_center(i, i)      # odd-length centers
            try_center(i, i + 1)  # even-length centers

        return ans
