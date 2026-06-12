class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(s)
        ans = 0
        for i in range(n):
            v = 0
            for j in range(i, n):
                v += s[j] in vowels
                c = (j - i + 1) - v
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans
