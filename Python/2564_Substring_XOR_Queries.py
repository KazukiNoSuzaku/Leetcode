class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        # Precompute first occurrence of each value (1..2^30) via substrings of length 1..30 with no leading 0.
        first = {}
        n = len(s)
        for i in range(n):
            if s[i] == '0':
                first.setdefault(0, [i, i])
                continue
            val = 0
            for j in range(i, min(i + 30, n)):
                val = (val << 1) | int(s[j])
                first.setdefault(val, [i, j])
        return [first.get(a ^ b, [-1, -1]) for a, b in queries]
