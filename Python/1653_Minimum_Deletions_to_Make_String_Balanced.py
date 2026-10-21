# Author: Kaustav Ghosh
# Problem: Minimum Deletions to Make String Balanced
# Approach: A string is balanced exactly when no 'b' appears before an 'a', which means the survivors form a block of a's followed by a block of b's, so the only thing to choose is where that boundary falls. For a given boundary the cost is every 'b' to its left plus every 'a' to its right, and sweeping the boundary from left to right lets both counts be maintained incrementally: moving past an 'a' removes one from the right-hand cost, and moving past a 'b' adds one to the left-hand cost. One pass over the string therefore evaluates every boundary.

class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        a_ahead = s.count('a')
        b_behind = 0
        best = a_ahead
        for ch in s:
            if ch == 'a':
                a_ahead -= 1
            else:
                b_behind += 1
            if b_behind + a_ahead < best:
                best = b_behind + a_ahead
        return best
