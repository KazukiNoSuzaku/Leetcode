# Author: Kaustav Ghosh
# Problem: Stone Game IX
# Approach: Only each stone's remainder on division by three matters, so the position is captured by how many stones leave remainder zero, one and two. Stones leaving remainder zero never change the running sum's remainder, so each one merely passes the turn along, meaning their count only matters through its parity. With an even count of those, the running sum must alternate between the two non-zero remainders and the first player can sustain that only by having at least one stone of each kind. With an odd count the turn order is flipped once, and the first player then needs a sufficiently lopsided supply of the two non-zero kinds, which works out to the counts differing by more than two.

class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        remainders = [0, 0, 0]
        for stone in stones:
            remainders[stone % 3] += 1
        if remainders[0] % 2 == 0:
            return remainders[1] >= 1 and remainders[2] >= 1
        difference = remainders[1] - remainders[2]
        if difference < 0:
            difference = -difference
        return difference > 2
