# Author: Kaustav Ghosh
# Problem: Find Longest Awesome Substring
# Approach: Bitmask parity of digit counts; a substring is rearrangeable to a palindrome if its mask matches an earlier prefix (all even) or differs by one bit (one odd)

class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_seen = {0: -1}
        mask = 0
        best = 0
        for i, c in enumerate(s):
            mask ^= 1 << int(c)
            # same parity prefix seen before -> all digit counts even between them
            if mask in first_seen:
                best = max(best, i - first_seen[mask])
            else:
                first_seen[mask] = i
            # allow exactly one digit with odd count (palindrome center)
            for b in range(10):
                target = mask ^ (1 << b)
                if target in first_seen:
                    best = max(best, i - first_seen[target])
        return best
