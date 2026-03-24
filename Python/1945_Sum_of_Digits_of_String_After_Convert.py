# Author: Kaustav Ghosh
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Convert to number string
        num_str = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            num_str = str(sum(int(d) for d in num_str))
        return int(num_str)
