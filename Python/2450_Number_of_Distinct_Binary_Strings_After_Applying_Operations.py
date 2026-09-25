# Author: Kaustav Ghosh
# Problem: Number of Distinct Binary Strings After Applying Operations
# Approach: There are n - k + 1 windows and applying one twice cancels, so a result is decided by which subset of windows is flipped. Different subsets always give different strings: position 0 is covered only by the first window, which pins its choice, then position 1 pins the second, and so on. So every subset is reachable and distinct, giving 2 ^ (n - k + 1)

class Solution(object):
    def countDistinctStrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return pow(2, len(s) - k + 1, 10 ** 9 + 7)
