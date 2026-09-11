# Author: Kaustav Ghosh
# Problem: Longest Binary Subsequence Less Than or Equal to K
# Approach: Every '0' can be taken for free (it never increases the value). For the '1's, only those in low-order positions matter: scan from the right, greedily including a '1' as long as adding its positional value keeps the running value <= k. Length is the count of zeros plus the includable ones

class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        zeros = s.count('0')
        ones = 0
        value = 0
        power = 1  # 2^position from the right
        for ch in reversed(s):
            if ch == '1':
                if value + power <= k:
                    value += power
                    ones += 1
                # once power exceeds k, no further '1' can be added
            power <<= 1
            if power > k:
                # remaining '1's to the left are too significant; stop counting ones
                break
        return zeros + ones
