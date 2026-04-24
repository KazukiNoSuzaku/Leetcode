class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events = []
        for l, r in intervals:
            events.append((l, 1))
            events.append((r + 1, -1))
        events.sort()
        ans = cur = 0
        for _, delta in events:
            cur += delta
            ans = max(ans, cur)
        return ans
