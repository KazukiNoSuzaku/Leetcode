# Author: Kaustav Ghosh
# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        m = len(s)
        result = []
        dirs = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

        for i in range(m):
            r, c = startPos[0], startPos[1]
            count = 0
            for j in range(i, m):
                dr, dc = dirs[s[j]]
                r += dr
                c += dc
                if 0 <= r < n and 0 <= c < n:
                    count += 1
                else:
                    break
            result.append(count)

        return result
