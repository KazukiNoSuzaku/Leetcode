# Author: Kaustav Ghosh
# Problem: Check if All A's Appears Before All B's
# Approach: Every a precedes every b exactly when the string never has a b immediately followed by an a, i.e. "ba" does not appear

class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return 'ba' not in s
