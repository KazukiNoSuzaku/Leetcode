# You are given a string s and an integer k. You can choose any character of the string
# and change it to any other uppercase English letter. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def characterReplacement(self, s, k):
        count = Counter()
        max_count = res = left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])
            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
