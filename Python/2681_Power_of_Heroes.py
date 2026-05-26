class Solution:
    def sumOfPower(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = s = 0
        for x in nums:
            ans = (ans + x * x % MOD * (x + s)) % MOD
            s = (2 * s + x) % MOD
        return ans
