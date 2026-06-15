from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(int)
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if s[j] != s[i]:
                    break
                count[(s[i], j - i + 1)] += 1
        ans = -1
        for (_, length), cnt in count.items():
            if cnt >= 3:
                ans = max(ans, length)
        return ans
