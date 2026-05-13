class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Max: remap first non-9 digit to 9. Min: remap first digit to 0.
        s = str(num)
        max_val = int(s.replace(next((c for c in s if c != '9'), s[0]), '9'))
        min_val = int(s.replace(s[0], '0'))
        return max_val - min_val
