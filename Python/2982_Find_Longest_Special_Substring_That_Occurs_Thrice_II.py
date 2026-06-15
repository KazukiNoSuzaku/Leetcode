from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        runs = defaultdict(list)
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            runs[s[i]].append(j - i)
            i = j

        def occurrences(char, k):
            return sum(max(0, r - k + 1) for r in runs[char])

        ans = -1
        for c in runs:
            lo, hi = 1, max(runs[c])
            while lo <= hi:
                mid = (lo + hi) // 2
                if occurrences(c, mid) >= 3:
                    ans = max(ans, mid)
                    lo = mid + 1
                else:
                    hi = mid - 1
        return ans
