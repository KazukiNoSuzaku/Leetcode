class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        seen = set()
        pairs = 0
        for w in words:
            if w[::-1] in seen:
                pairs += 1
            else:
                seen.add(w)
        return pairs
