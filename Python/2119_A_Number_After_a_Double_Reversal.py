# Author: Kaustav Ghosh
# Problem: A Number After a Double Reversal
# Approach: Reversing drops trailing zeros, so a double reversal recovers the number only when it has no trailing zero, except zero itself which is unaffected

class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == 0 or num % 10 != 0
