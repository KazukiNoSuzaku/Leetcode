class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        t = 1
        while True:
            start = t * k
            if start >= n:
                return t
            # After t operations, word[start:] must be a prefix of the original word
            if word[:n - start] == word[start:]:
                return t
            t += 1
