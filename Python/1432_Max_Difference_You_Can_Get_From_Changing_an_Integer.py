# Author: Kaustav Ghosh
# Problem: Max Difference You Can Get From Changing an Integer (Premium)
# Approach: Replace one digit to maximize and another to minimize

class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        # Maximize: find first digit that is not 9, replace all occurrences with 9
        a = s
        for d in s:
            if d != '9':
                a = s.replace(d, '9')
                break

        # Minimize: if first digit != 1, replace all its occurrences with 1
        # else find first non-0, non-1 digit after first, replace with 0
        b = s
        if s[0] != '1':
            b = s.replace(s[0], '1')
        else:
            for d in s[1:]:
                if d != '0' and d != '1':
                    b = s.replace(d, '0')
                    break

        return int(a) - int(b)
