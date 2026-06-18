class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        # Start with bits above n (fixed, can't be changed by x)
        ax = a >> n << n
        bx = b >> n << n
        for i in range(n - 1, -1, -1):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            if a_bit == b_bit:
                # Both same: set x_i to make both bits 1 (maximizes both values)
                ax |= (1 << i)
                bx |= (1 << i)
            else:
                # One is 0, one is 1; give the 1-bit to the smaller value to equalize
                if ax <= bx:
                    ax |= (1 << i)
                    bx &= ~(1 << i)
                else:
                    bx |= (1 << i)
                    ax &= ~(1 << i)
        return (ax % MOD) * (bx % MOD) % MOD
