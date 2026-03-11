# In a row of dominoes, find minimum rotations so all top or all bottom values are equal.

# Author: Kaustav Ghosh

class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        def check(x):
            top_rot = bot_rot = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return float('inf')
                elif t != x:
                    top_rot += 1
                elif b != x:
                    bot_rot += 1
            return min(top_rot, bot_rot)
        res = min(check(tops[0]), check(bottoms[0]))
        return res if res != float('inf') else -1
