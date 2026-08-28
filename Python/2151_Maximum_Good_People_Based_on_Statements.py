# Author: Kaustav Ghosh
# Problem: Maximum Good People Based on Statements
# Approach: Try every assignment of good/bad to the n people. Good people always tell the truth, so each good person's statements must match the assignment; bad people's statements are ignored. Track the largest good count among consistent assignments

class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        n = len(statements)
        best = 0
        for mask in range(1 << n):
            valid = True
            for i in range(n):
                if not (mask >> i & 1):
                    continue  # bad person, statements ignored
                for j in range(n):
                    s = statements[i][j]
                    if s == 1 and not (mask >> j & 1):
                        valid = False
                        break
                    if s == 0 and (mask >> j & 1):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                best = max(best, bin(mask).count('1'))
        return best
