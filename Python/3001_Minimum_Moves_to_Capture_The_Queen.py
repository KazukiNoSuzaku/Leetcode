class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # Rook at (a,b), bishop at (c,d), queen at (e,f)
        # Rook attacks along row/column unless bishop blocks
        if a == e:
            lo, hi = min(b, f), max(b, f)
            if not (c == a and lo < d < hi):
                return 1
        if b == f:
            lo, hi = min(a, e), max(a, e)
            if not (d == b and lo < c < hi):
                return 1

        # Bishop attacks along diagonal unless rook blocks
        if abs(c - e) == abs(d - f):
            steps = abs(c - e)
            dx = 1 if e > c else -1
            dy = 1 if f > d else -1
            blocked = any(c + i * dx == a and d + i * dy == b for i in range(1, steps))
            if not blocked:
                return 1

        return 2
