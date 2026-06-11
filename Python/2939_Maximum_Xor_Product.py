class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        mask = (1 << n) - 1
        fa, fb = a >> n, b >> n
        ra, rb = 0, 0

        for i in range(n - 1, -1, -1):
            ba, bb = (a >> i) & 1, (b >> i) & 1
            if ba == bb:
                ra |= (1 << i)
                rb |= (1 << i)
            else:
                curr_a = (fa << n) | ra
                curr_b = (fb << n) | rb
                if curr_a <= curr_b:
                    ra |= (1 << i)
                else:
                    rb |= (1 << i)

        A = (fa << n) | ra
        B = (fb << n) | rb
        return (A % MOD) * (B % MOD) % MOD
