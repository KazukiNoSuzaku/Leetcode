class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 10 ** 9 + 7
        powers = []
        bit = 0
        while n:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1
        ans = []
        for l, r in queries:
            prod = 1
            for i in range(l, r + 1):
                prod = prod * powers[i] % MOD
            ans.append(prod)
        return ans
