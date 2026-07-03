# Author: Kaustav Ghosh
# Problem: Split a String Into the Max Number of Unique Substrings
# Approach: Backtrack over every cut, keeping a set of used pieces; prune when the best-possible remaining count cannot beat the current best

class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        self.best = 0
        seen = set()

        def backtrack(start):
            # Even if every remaining char became its own unique piece, could we beat best?
            if len(seen) + (n - start) <= self.best:
                return
            if start == n:
                self.best = max(self.best, len(seen))
                return
            for end in range(start + 1, n + 1):
                piece = s[start:end]
                if piece not in seen:
                    seen.add(piece)
                    backtrack(end)
                    seen.remove(piece)

        backtrack(0)
        return self.best
