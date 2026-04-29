class Solution:
    def countDistinct(self, s: str, k: int) -> int:
        # Each operation flips any k consecutive chars; two strings are equivalent
        # iff they differ only in patterns reachable by such flips.
        # The number of distinct reachable strings from any starting string is 2^(n-k+1),
        # because we have n-k+1 independent flip positions.
        MOD = 10 ** 9 + 7
        n = len(s)
        return pow(2, n - k + 1, MOD)
