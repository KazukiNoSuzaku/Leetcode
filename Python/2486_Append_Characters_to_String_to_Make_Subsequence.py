class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for c in s:
            if j < len(t) and c == t[j]:
                j += 1
        return len(t) - j
