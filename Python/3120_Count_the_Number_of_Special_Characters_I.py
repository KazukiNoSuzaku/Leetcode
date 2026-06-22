class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        return sum(1 for c in 'abcdefghijklmnopqrstuvwxyz' if c in s and c.upper() in s)
