# Author: Kaustav Ghosh
# Problem: 2151. Maximum Good People Based on Statements
# URL: https://leetcode.com/problems/maximum-good-people-based-on-statements/
# Approach: Bitmask enumerate all possible assignments of good/bad people

class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        n = len(statements)
        ans = 0
        for mask in range(1 << n):
            # mask represents which people are "good"
            good_people = [i for i in range(n) if mask & (1 << i)]
            valid = True
            for g in good_people:
                for j in range(n):
                    stmt = statements[g][j]
                    if stmt == 1 and not (mask & (1 << j)):
                        valid = False
                        break
                    if stmt == 0 and (mask & (1 << j)):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                ans = max(ans, len(good_people))
        return ans
