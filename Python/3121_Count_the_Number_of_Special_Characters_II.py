class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        for i, c in enumerate(word):
            if c.islower():
                last_lower[c] = i
            else:
                if c.lower() not in first_upper:
                    first_upper[c.lower()] = i
        return sum(
            1 for c in last_lower
            if c in first_upper and last_lower[c] < first_upper[c]
        )
