# Author: Kaustav Ghosh
# Problem: Minimum Moves to Reach Target Score
# Approach: Work backward from the target. While doubles remain, halve when the value is even (undoing a double) and decrement when odd (undoing an increment). Once doubles are used up, the rest are increments down to 1

class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        moves = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 1:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            moves += 1
        return moves + (target - 1)
