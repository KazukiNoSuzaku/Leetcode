from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = ans = 0
        for right, c in enumerate(s):
            count[c] += 1
            while count[c] > 2:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
