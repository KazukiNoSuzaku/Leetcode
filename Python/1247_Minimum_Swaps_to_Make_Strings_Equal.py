# Author: Kaustav Ghosh
# Count xy and yx mismatches; each pair of same type costs 1 swap, mixed pair costs 2

class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        if (xy + yx) % 2 == 1:
            return -1
        return xy // 2 + yx // 2 + (xy % 2) * 2
