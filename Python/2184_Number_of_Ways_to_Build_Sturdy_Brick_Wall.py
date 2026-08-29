# Author: Kaustav Ghosh
# Problem: Number of Ways to Build Sturdy Brick Wall
# Approach: Enumerate every valid single row as a composition of the width using the available brick lengths, recording its internal seam positions as a bitmask. Two rows can be stacked adjacently only if their seam masks are disjoint. DP row by row over the height, accumulating counts of walls ending in each row configuration

class Solution(object):
    def buildWall(self, height, width, bricks):
        """
        :type height: int
        :type width: int
        :type bricks: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        widths = sorted(set(b for b in bricks if b <= width))

        rows = []  # seam bitmask for each valid row

        def build(pos, mask):
            if pos == width:
                rows.append(mask)
                return
            for b in widths:
                np = pos + b
                if np > width:
                    break
                # add an internal seam at np (unless it's the far edge)
                nmask = mask | (1 << np) if np < width else mask
                build(np, nmask)

        build(0, 0)

        # dp[r] = number of walls built so far whose top row is rows[r]
        dp = [1] * len(rows)
        for _ in range(height - 1):
            ndp = [0] * len(rows)
            for j in range(len(rows)):
                mj = rows[j]
                total = 0
                for i in range(len(rows)):
                    if rows[i] & mj == 0:
                        total += dp[i]
                ndp[j] = total % MOD
            dp = ndp
        return sum(dp) % MOD
