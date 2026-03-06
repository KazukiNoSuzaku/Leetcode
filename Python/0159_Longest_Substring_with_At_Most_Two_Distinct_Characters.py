# Given a string s, return the length of the longest substring that contains at most
# two distinct characters.

# Example 1:
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.

# Example 2:
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.

# Constraints:
# 1 <= s.length <= 10^5
# s consists of English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        count = {}
        left = 0
        res = 0
        for right, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while len(count) > 2:
                lc = s[left]
                count[lc] -= 1
                if count[lc] == 0:
                    del count[lc]
                left += 1
            res = max(res, right - left + 1)
        return res
