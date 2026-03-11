# Find which receptor a laser ray hits in a mirrored room.

# Author: Kaustav Ghosh

import math

class Solution(object):
    def mirrorReflection(self, p, q):
        g = math.gcd(p, q)
        p //= g; q //= g
        if p % 2 == 0: return 2
        if q % 2 == 0: return 0
        return 1
