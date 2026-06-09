class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # Need >= 1 'l', >= 1 't', >= 2 'e' — inclusion-exclusion over missing characters
        total = pow(26, n, MOD)
        a  = pow(25, n, MOD)                                    # no 'l'
        b  = pow(25, n, MOD)                                    # no 't'
        c  = (pow(25, n, MOD) + n * pow(25, n - 1, MOD)) % MOD # < 2 'e'
        ab = pow(24, n, MOD)
        ac = (pow(24, n, MOD) + n * pow(24, n - 1, MOD)) % MOD
        bc = (pow(24, n, MOD) + n * pow(24, n - 1, MOD)) % MOD
        abc = (pow(23, n, MOD) + n * pow(23, n - 1, MOD)) % MOD
        return (total - a - b - c + ab + ac + bc - abc) % MOD
