# Author: Kaustav Ghosh
# Problem: Substring With Largest Variance
# Approach: For each ordered pair of distinct characters (a, b), maximize (count_a - count_b) over substrings that contain at least one b, treating a as +1 and b as -1 in a Kadane sweep. When the running difference drops below zero it resets, but a dropped b lets a b-free prefix still count as if one b were carried, which keeps the "at least one b" requirement satisfiable

class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set(s)
        best = 0
        for a in chars:
            for b in chars:
                if a == b:
                    continue
                ca = cb = 0
                dropped_b = False  # we discarded a prefix that contained a b
                for ch in s:
                    if ch == a:
                        ca += 1
                    elif ch == b:
                        cb += 1
                    if cb > 0:
                        best = max(best, ca - cb)
                    elif dropped_b and ca > 0:
                        # no b in current window, but one is available from the drop
                        best = max(best, ca - 1)
                    if ca < cb:
                        ca = cb = 0
                        dropped_b = True
        return best
