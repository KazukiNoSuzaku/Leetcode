# Author: Kaustav Ghosh
# From king position, scan 8 directions for the first queen

class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queen_set = {(r, c) for r, c in queens}
        result = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = king[0] + dr, king[1] + dc
                while 0 <= r < 8 and 0 <= c < 8:
                    if (r, c) in queen_set:
                        result.append([r, c])
                        break
                    r += dr
                    c += dc
        return result
