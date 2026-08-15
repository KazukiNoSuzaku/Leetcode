# Author: Kaustav Ghosh
# Problem: Minimum Moves to Convert String
# Approach: Scan left to right. Whenever an 'X' appears, one move covers it and the next two positions, so jump ahead by three; otherwise advance by one

class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1
        return moves
