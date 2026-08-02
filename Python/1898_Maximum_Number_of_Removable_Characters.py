# Author: Kaustav Ghosh
# Problem: Maximum Number of Removable Characters
# Approach: Feasibility is monotonic in k (removing more can only hurt), so binary search k and check if p remains a subsequence after marking the first k removable indices deleted

class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        def still_subsequence(k):
            removed = set(removable[:k])
            j = 0
            for i, ch in enumerate(s):
                if i in removed:
                    continue
                if j < len(p) and ch == p[j]:
                    j += 1
            return j == len(p)

        lo, hi = 0, len(removable)
        best = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if still_subsequence(mid):
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return best
