# Place students in seats so no cheating (no adjacent or diagonal visibility).
# Return the maximum number of students that can take the exam.

# Author: Kaustav Ghosh

class Solution(object):
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        rows = [int(''.join('1' if seats[i][j] == '.' else '0' for j in range(n)), 2)
                for i in range(m)]
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(row, prev_mask):
            if row == m:
                return 0
            valid = rows[row]
            best = 0
            mask = valid
            while True:
                # mask is subset of valid with no two adjacent seats
                if (mask & (mask >> 1)) == 0:
                    # no conflict with previous row (no upper-left or upper-right)
                    if (mask & (prev_mask >> 1)) == 0 and (mask & (prev_mask << 1)) == 0:
                        best = max(best, bin(mask).count('1') + dp(row + 1, mask))
                if mask == 0:
                    break
                mask = (mask - 1) & valid
            return best
        return dp(0, 0)
