# Count how many n have exactly k trailing zeroes in n!.

# Author: Kaustav Ghosh

class Solution(object):
    def preimageSizeFZF(self, k):
        def trailing_zeroes(n):
            count = 0
            while n >= 5:
                n //= 5
                count += n
            return count
        def leftmost(k):
            lo, hi = 0, 5 * (k + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                if trailing_zeroes(mid) < k: lo = mid + 1
                else: hi = mid
            return lo
        return leftmost(k + 1) - leftmost(k)
