# Author: Kaustav Ghosh
# Problem: Check If a String Contains All Binary Codes of Size K
# Approach: Collect all k-length substrings, check if count equals 2^k

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i + k])
        return len(seen) == (1 << k)
