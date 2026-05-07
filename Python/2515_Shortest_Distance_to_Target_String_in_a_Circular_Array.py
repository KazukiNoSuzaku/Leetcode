class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        # Scan all occurrences of target; return min circular distance from startIndex.
        n = len(words)
        ans = n
        for i, w in enumerate(words):
            if w == target:
                d = abs(i - startIndex)
                ans = min(ans, d, n - d)
        return ans if ans < n else -1
