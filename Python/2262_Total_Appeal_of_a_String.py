# Author: Kaustav Ghosh
# Problem: 2262. Total Appeal of A String
# URL: https://leetcode.com/problems/total-appeal-of-a-string/
# Difficulty: Hard
#
# Approach:
# For each character at index i, its contribution to all substrings ending at i
# is (i - last_seen[c]) where last_seen[c] is the last index where c appeared.
# Accumulate this running appeal across all indices.

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        total = 0
        cur = 0
        for i, c in enumerate(s):
            cur += i - last_seen.get(c, -1)
            total += cur
            last_seen[c] = i
        return total
