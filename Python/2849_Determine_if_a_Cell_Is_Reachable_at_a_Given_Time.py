class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        d = max(abs(fx - sx), abs(fy - sy))
        if d == 0:
            return t != 1
        return t >= d
