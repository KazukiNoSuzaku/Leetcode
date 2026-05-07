class Solution:
    def captureForts(self, forts: list[int]) -> int:
        # Track the last non-zero position; count zeros between a 1 and -1 (or vice-versa).
        ans = 0
        prev = -1
        for i, f in enumerate(forts):
            if f != 0:
                if prev != -1 and forts[prev] != f:
                    ans = max(ans, i - prev - 1)
                prev = i
        return ans
