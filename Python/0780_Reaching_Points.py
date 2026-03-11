# Check if (sx,sy) can reach (tx,ty) by repeatedly adding one coord to other.

# Author: Kaustav Ghosh

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy: return True
            if tx > ty:
                if ty == sy: return (tx - sx) % ty == 0
                tx %= ty
            else:
                if tx == sx: return (ty - sy) % tx == 0
                ty %= tx
        return False
