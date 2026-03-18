# Author: Kaustav Ghosh
# Problem: 1593 - Split a String Into the Max Number of Unique Substrings
# Approach: Backtracking with set

class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.result = 0

        def backtrack(start, seen):
            if start == len(s):
                self.result = max(self.result, len(seen))
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub not in seen:
                    seen.add(sub)
                    backtrack(end, seen)
                    seen.remove(sub)

        backtrack(0, set())
        return self.result
