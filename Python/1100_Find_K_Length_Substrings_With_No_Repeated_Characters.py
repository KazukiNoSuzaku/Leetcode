# Author: Kaustav Ghosh
# 1100. Find K-Length Substrings With No Repeated Characters
# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k > len(s):
            return 0
        count = {}
        result = 0
        lo = 0
        for hi in range(len(s)):
            c = s[hi]
            count[c] = count.get(c, 0) + 1
            while count[c] > 1:
                count[s[lo]] -= 1
                if count[s[lo]] == 0:
                    del count[s[lo]]
                lo += 1
            if hi - lo + 1 == k:
                result += 1
                count[s[lo]] -= 1
                if count[s[lo]] == 0:
                    del count[s[lo]]
                lo += 1
        return result
