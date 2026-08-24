# Author: Kaustav Ghosh
# Problem: Execution of All Suffix Instructions Staying in a Grid
# Approach: For each starting index, simulate the instructions from there, moving until a step would leave the grid, and record how many executed

class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        m = len(s)
        answer = [0] * m
        for i in range(m):
            r, c = startPos
            count = 0
            for j in range(i, m):
                dr, dc = moves[s[j]]
                r += dr
                c += dc
                if 0 <= r < n and 0 <= c < n:
                    count += 1
                else:
                    break
            answer[i] = count
        return answer
