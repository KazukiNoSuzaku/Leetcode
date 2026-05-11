class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        # Prefix sum: mark words that start and end with a vowel; answer each query in O(1).
        vowels = set('aeiou')
        prefix = [0] * (len(words) + 1)
        for i, w in enumerate(words):
            prefix[i + 1] = prefix[i] + (w[0] in vowels and w[-1] in vowels)
        return [prefix[r + 1] - prefix[l] for l, r in queries]
