class Solution:
    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        pos = sorted(nums[i] + d * (1 if s[i] == 'R' else -1) for i in range(len(nums)))
        ans = prefix = 0
        for i, x in enumerate(pos):
            ans = (ans + i * x - prefix) % MOD
            prefix += x
        return ans
