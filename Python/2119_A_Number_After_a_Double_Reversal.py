# Author: Kaustav Ghosh
# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == 0 or num % 10 != 0
