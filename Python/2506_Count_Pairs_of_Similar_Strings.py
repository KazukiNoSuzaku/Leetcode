from collections import Counter

class Solution:
    def similarPairs(self, words: list[str]) -> int:
        # Two words are similar iff they have the same character set; count pairs via frequency.
        freq = Counter(frozenset(w) for w in words)
        return sum(v * (v - 1) // 2 for v in freq.values())
