from collections import defaultdict

class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        # Premium: count substrings where count('1') * num2 == count('0') * num1.
        # Running score: +num2 per '1', -num1 per '0'.
        # Substring [l,r] is valid iff prefix[r+1] == prefix[l] (net score = 0).
        counts = defaultdict(int)
        counts[0] = 1
        score = ans = 0
        for c in s:
            score += num2 if c == '1' else -num1
            ans += counts[score]
            counts[score] += 1
        return ans
