# Author: Kaustav Ghosh
# Problem: Append Characters to String to Make Subsequence
# Approach: Characters can only be added at the end, so the prefix of t already covered is whatever greedily matches inside s. Walk s once advancing a pointer through t, and append whatever is left of t

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        matched = 0
        for ch in s:
            if matched < len(t) and ch == t[matched]:
                matched += 1
        return len(t) - matched
