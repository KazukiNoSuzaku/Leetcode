from collections import Counter
import bisect

class Solution:
    def countExcellentPairs(self, nums: list[int], k: int) -> int:
        # popcount(a|b) + popcount(a&b) = popcount(a) + popcount(b)
        counts = sorted(bin(n).count('1') for n in set(nums))
        ans = 0
        for i, c in enumerate(counts):
            need = k - c
            ans += len(counts) - bisect.bisect_left(counts, need)
        return ans
