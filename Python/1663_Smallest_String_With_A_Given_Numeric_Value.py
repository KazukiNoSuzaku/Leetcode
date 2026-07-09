# Author: Kaustav Ghosh
# Problem: Smallest String With A Given Numeric Value
# Approach: Start with all 'a' (value 1 each), then greedily push the rightmost letters up to 'z' to absorb the leftover value

class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ['a'] * n
        k -= n  # every slot already contributes 1
        i = n - 1
        while k > 0:
            add = min(25, k)  # bump this slot from 'a' up to at most 'z'
            res[i] = chr(ord('a') + add)
            k -= add
            i -= 1
        return ''.join(res)
