# Author: Kaustav Ghosh
# Problem: Split a String Into the Max Number of Unique Substrings
# Approach: The string is at most sixteen characters, so there are only 2^15 places to cut and a backtracking search over cut points is affordable: at each position I try every next piece, keep it only if it has not been used, recurse, and undo. Two cheap prunings keep it quick, namely stopping when even taking every remaining character as its own piece could not beat the best found so far, and the fact that single characters bound the answer, so the search never explores the many branches that cannot win.

class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        used = set()
        self.best = 0

        def search(start, count):
            if start == n:
                if count > self.best:
                    self.best = count
                return
            # Even one piece per remaining character could not beat the best.
            if count + (n - start) <= self.best:
                return
            for end in range(start + 1, n + 1):
                piece = s[start:end]
                if piece not in used:
                    used.add(piece)
                    search(end, count + 1)
                    used.discard(piece)

        search(0, 0)
        return self.best
