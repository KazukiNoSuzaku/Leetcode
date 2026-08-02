# Author: Kaustav Ghosh
# Problem: The Earliest and Latest Rounds Where Players Compete
# Approach: Recurse on (players, positions f<s from the left). If paired they meet now; otherwise enumerate how many players ahead of each survive to the next (halved) bracket. Three cases for s - front, middle, or back - place it correctly among the survivors

from functools import lru_cache

class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        @lru_cache(maxsize=None)
        def dp(size, f, s):
            if f > s:
                f, s = s, f
            if f + s == size + 1:
                return (1, 1)
            if f + s > size + 1:  # mirror so f + s <= size + 1
                f, s = size + 1 - s, size + 1 - f

            half = (size + 1) // 2
            earliest = float('inf')
            latest = float('-inf')

            def consider(a, b):
                e, l = dp(half, a, b)
                return e, l

            if 2 * s < size + 1:            # s is a front player
                for i in range(f):
                    for j in range(s - f):
                        e, l = consider(i + 1, i + j + 2)
                        earliest = min(earliest, e + 1)
                        latest = max(latest, l + 1)
            elif 2 * s == size + 1:         # s is the middle (odd size)
                for i in range(f):
                    for j in range((size - 1) // 2 - f + 1):
                        e, l = consider(i + 1, i + j + 2)
                        earliest = min(earliest, e + 1)
                        latest = max(latest, l + 1)
            else:                           # s is a back player
                s_mirror = size + 1 - s
                offset = half - s_mirror    # survivors guaranteed to sit before s
                for i in range(f):
                    for j in range(s_mirror - f):
                        e, l = consider(i + 1, i + j + offset + 2)
                        earliest = min(earliest, e + 1)
                        latest = max(latest, l + 1)

            return (earliest, latest)

        return list(dp(n, firstPlayer, secondPlayer))
