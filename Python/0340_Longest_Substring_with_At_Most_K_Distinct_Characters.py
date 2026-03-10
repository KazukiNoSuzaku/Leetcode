# Given a string s and an integer k, return the length of the longest substring of s that
# contains at most k distinct characters.

# Example 1:
# Input: s = "eceba", k = 2
# Output: 3

# Example 2:
# Input: s = "aa", k = 1
# Output: 2

# Constraints:
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 50

# Author: Kaustav Ghosh

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        count = {}
        left = res = 0
        for right, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while len(count) > k:
                lc = s[left]
                count[lc] -= 1
                if count[lc] == 0:
                    del count[lc]
                left += 1
            res = max(res, right - left + 1)
        return res
