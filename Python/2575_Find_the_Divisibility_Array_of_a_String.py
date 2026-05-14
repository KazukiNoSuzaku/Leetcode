class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        # Track running modulo to avoid computing the actual huge number.
        cur = 0
        result = []
        for ch in word:
            cur = (cur * 10 + int(ch)) % m
            result.append(1 if cur == 0 else 0)
        return result
