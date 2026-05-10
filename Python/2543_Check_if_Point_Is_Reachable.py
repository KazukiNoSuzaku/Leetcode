from math import gcd

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        # Operations (x,y)→(x+y,y)|(x,x+y) preserve gcd; halving ops allow any power-of-2 gcd.
        # Reachable from (1,1) iff gcd(targetX, targetY) is a power of 2.
        g = gcd(targetX, targetY)
        return g & (g - 1) == 0
