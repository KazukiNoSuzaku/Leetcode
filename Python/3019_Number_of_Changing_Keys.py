class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum(1 for i in range(1, len(s)) if s[i] != s[i - 1])
