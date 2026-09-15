# Author: Kaustav Ghosh
# Problem: First Letter to Appear Twice
# Approach: Scan the string once keeping the set of letters already seen; the first letter that is already in the set is the answer

class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
        return ""
