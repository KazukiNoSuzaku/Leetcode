# Author: Kaustav Ghosh
# Problem: Find Longest Awesome Substring
# Approach: A substring can be rearranged into a palindrome exactly when at most one digit occurs an odd number of times, which depends only on the parity of each digit's count. Track those ten parities as a bitmask over the prefix and remember where each mask first appeared; a substring is awesome when its two end masks are equal, or differ in exactly one bit

class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_seen = {0: -1}
        mask = 0
        best = 0
        for i, ch in enumerate(s):
            mask ^= 1 << int(ch)
            if mask in first_seen:
                best = max(best, i - first_seen[mask])
            else:
                first_seen[mask] = i
            for digit in range(10):
                candidate = mask ^ (1 << digit)
                if candidate in first_seen:
                    best = max(best, i - first_seen[candidate])
        return best
