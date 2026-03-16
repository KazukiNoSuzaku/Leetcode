# Author: Kaustav Ghosh
# Problem: Construct K Palindrome Strings
# Approach: Count odd-frequency chars, need <= k <= n

from collections import Counter

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k > len(s):
            return False
        odd_count = sum(1 for v in Counter(s).values() if v % 2 == 1)
        return odd_count <= k
