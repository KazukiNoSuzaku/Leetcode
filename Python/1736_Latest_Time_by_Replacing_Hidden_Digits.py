# Author: Kaustav Ghosh
# Problem: Latest Time by Replacing Hidden Digits
# Approach: Later times are decided by the earlier digits first, so each position takes the largest digit that still leaves a valid time, and the only coupling is within the hour: the tens digit may be two only when the units digit permits it, which means looking ahead at the units digit before settling the tens. Once the tens digit is fixed, the units digit's ceiling follows from it, three when the hour starts with a two and nine otherwise. The minutes are independent of everything, so a hidden tens digit is always five and a hidden units digit always nine.

class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = list(time)
        if digits[0] == '?':
            # Two is only safe if the units digit allows it.
            digits[0] = '2' if digits[1] in '?0123' else '1'
        if digits[1] == '?':
            digits[1] = '3' if digits[0] == '2' else '9'
        if digits[3] == '?':
            digits[3] = '5'
        if digits[4] == '?':
            digits[4] = '9'
        return ''.join(digits)
