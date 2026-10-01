# Author: Kaustav Ghosh
# Problem: Take K of Each Character From Left and Right
# Approach: Whatever is taken forms a prefix and a suffix, so what stays is one contiguous middle stretch. Taking the fewest characters means leaving the longest middle whose complement still holds k of each letter, which a sliding window finds; the answer is the length minus that window

from collections import Counter


class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        totals = Counter(s)
        if any(totals[ch] < k for ch in "abc"):
            return -1
        inside = Counter()
        left = 0
        longest = 0
        for right, ch in enumerate(s):
            inside[ch] += 1
            while any(totals[c] - inside[c] < k for c in "abc"):
                inside[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return len(s) - longest
