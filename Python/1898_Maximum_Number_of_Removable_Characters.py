# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        def canRemove(k):
            removed = set(removable[:k])
            j = 0
            for i in range(len(s)):
                if i in removed:
                    continue
                if j < len(p) and s[i] == p[j]:
                    j += 1
            return j == len(p)

        lo, hi = 0, len(removable)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if canRemove(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
