class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        def val(s: str) -> int:
            return int(s) if s.isdigit() else len(s)
        return max(val(s) for s in strs)
