class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted(c for c in s if c in 'aeiouAEIOU')
        res = list(s)
        j = 0
        for i, c in enumerate(res):
            if c in 'aeiouAEIOU':
                res[i] = vowels[j]
                j += 1
        return ''.join(res)
