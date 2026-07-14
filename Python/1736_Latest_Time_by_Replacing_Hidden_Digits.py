# Author: Kaustav Ghosh
# Problem: Latest Time by Replacing Hidden Digits
# Approach: Fill each hidden digit with the largest value still valid; the hour's first digit depends on the second (2 only if the second allows 20-23)

class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        t = list(time)
        if t[0] == '?':
            t[0] = '2' if t[1] in '?0123' else '1'
        if t[1] == '?':
            t[1] = '3' if t[0] == '2' else '9'
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        return ''.join(t)
