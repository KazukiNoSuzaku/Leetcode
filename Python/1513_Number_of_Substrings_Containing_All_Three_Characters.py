# Author: Kaustav Ghosh
# Problem: Number of Substrings Containing All Three Characters
# Approach: Track last-seen index of each char; valid substrings ending at i = min(last_seen) + 1

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {'a': -1, 'b': -1, 'c': -1}
        ans = 0
        for i, c in enumerate(s):
            last[c] = i
            ans += min(last.values()) + 1
        return ans
