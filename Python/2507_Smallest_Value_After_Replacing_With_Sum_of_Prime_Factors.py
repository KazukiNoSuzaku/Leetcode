class Solution:
    def smallestValue(self, n: int) -> int:
        # Repeatedly replace n with the sum of its prime factors (with repetition) until fixpoint.
        while True:
            s, d, temp = 0, 2, n
            while d * d <= temp:
                while temp % d == 0:
                    s += d
                    temp //= d
                d += 1
            s += temp if temp > 1 else 0
            if s == n:
                return n
            n = s
