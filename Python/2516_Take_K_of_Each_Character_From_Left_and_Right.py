from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Sliding window maximizing removable middle; shrink when any char falls below k in remainder.
        total = Counter(s)
        if any(total[c] < k for c in 'abc'):
            return -1
        n = len(s)
        window = Counter()
        ans = l = 0
        for r in range(n):
            window[s[r]] += 1
            while any(total[c] - window[c] < k for c in 'abc'):
                window[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return n - ans
