class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        first = {}
        for i, ch in enumerate(s):
            if ch in first:
                if i - first[ch] - 1 != distance[ord(ch) - ord('a')]:
                    return False
            else:
                first[ch] = i
        return True
