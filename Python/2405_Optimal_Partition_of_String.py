class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        parts = 1
        for ch in s:
            if ch in seen:
                parts += 1
                seen = set()
            seen.add(ch)
        return parts
