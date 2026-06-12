from collections import defaultdict

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        # Beautiful: vowels == consonants == v and v*v % k == 0.
        # v*v % k == 0 iff v is a multiple of r = prod(p^ceil(e/2)) over k's
        # prime factors, so the length must be a multiple of L = 2r.
        factors = {}
        temp, d = k, 2
        while d * d <= temp:
            while temp % d == 0:
                factors[d] = factors.get(d, 0) + 1
                temp //= d
            d += 1
        if temp > 1:
            factors[temp] = factors.get(temp, 0) + 1
        r = 1
        for p, e in factors.items():
            r *= p ** ((e + 1) // 2)
        L = 2 * r

        # Substring (j, i] works iff prefix diffs match and (i - j) % L == 0.
        vowels = set('aeiou')
        count = defaultdict(int)
        count[(0, 0)] = 1
        diff = ans = 0
        for i, ch in enumerate(s, 1):
            diff += 1 if ch in vowels else -1
            key = (diff, i % L)
            ans += count[key]
            count[key] += 1
        return ans
