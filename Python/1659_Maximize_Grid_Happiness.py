# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximize-grid-happiness/

class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        from functools import lru_cache

        def cost(state, neighbor):
            # state: 0=empty, 1=introvert, 2=extrovert
            if state == 0 or neighbor == 0:
                return 0
            val = 0
            if state == 1:
                val -= 30
            else:
                val += 20
            if neighbor == 1:
                val -= 30
            else:
                val += 20
            return val

        @lru_cache(None)
        def dp(pos, intro, extro, prev_row):
            if pos == m * n or (intro == 0 and extro == 0):
                return 0
            r, c = divmod(pos, n)
            up = prev_row[0] if prev_row else 0
            left = 0
            # We track previous row as tuple of n values
            res = dp(pos + 1, intro, extro, prev_row[1:] + (0,))  # empty
            if intro > 0:
                gain = 120
                if r > 0:
                    gain += cost(1, up)
                if c > 0:
                    gain += cost(1, left)
                # Wait, need to track left neighbor too
                pass
            return res

        # Use profile DP with bitmask for row states
        # Simpler approach for small grid
        total = m * n
        three_n = 3 ** n

        def encode(row_state):
            val = 0
            for s in row_state:
                val = val * 3 + s
            return val

        def decode(val):
            row = []
            for _ in range(n):
                row.append(val % 3)
                val //= 3
            return row[::-1]

        memo = {}

        def solve(row, intro, extro, prev):
            if row == m:
                return 0
            if (row, intro, extro, prev) in memo:
                return memo[(row, intro, extro, prev)]

            prev_decoded = decode(prev)
            best = [0]

            def fill(col, intro_left, extro_left, curr_row, happiness):
                if col == n:
                    encoded = encode(curr_row)
                    val = happiness + solve(row + 1, intro_left, extro_left, encoded)
                    best[0] = max(best[0], val)
                    return

                # Empty
                fill(col + 1, intro_left, extro_left, curr_row + [0], happiness)

                # Introvert
                if intro_left > 0:
                    h = 120
                    if col > 0 and curr_row[col - 1] != 0:
                        h += cost(1, curr_row[col - 1])
                    if prev_decoded[col] != 0:
                        h += cost(1, prev_decoded[col])
                    fill(col + 1, intro_left - 1, extro_left, curr_row + [1], happiness + h)

                # Extrovert
                if extro_left > 0:
                    h = 40
                    if col > 0 and curr_row[col - 1] != 0:
                        h += cost(2, curr_row[col - 1])
                    if prev_decoded[col] != 0:
                        h += cost(2, prev_decoded[col])
                    fill(col + 1, intro_left, extro_left - 1, curr_row + [2], happiness + h)

            fill(0, intro, extro, [], 0)
            memo[(row, intro, extro, prev)] = best[0]
            return best[0]

        return solve(0, introvertsCount, extrovertsCount, 0)
