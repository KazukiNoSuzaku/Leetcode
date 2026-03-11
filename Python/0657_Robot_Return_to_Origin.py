# Determine if a robot returns to the origin after executing a series of moves.

# Author: Kaustav Ghosh

class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
