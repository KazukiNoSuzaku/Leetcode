# Author: Kaustav Ghosh
# Problem: Perform String Shifts (Premium)
# Approach: Sum all shifts (left=negative, right=positive), apply net shift mod len

class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        net = 0
        for direction, amount in shift:
            if direction == 0:
                net -= amount
            else:
                net += amount
        net %= len(s)
        return s[-net:] + s[:-net] if net else s
