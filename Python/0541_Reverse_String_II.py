# Given a string s and an integer k, reverse the first k characters for every 2k characters.
# If fewer than k characters remain, reverse all of them.

# Author: Kaustav Ghosh

class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = s[i:i+k][::-1]
        return ''.join(s)
