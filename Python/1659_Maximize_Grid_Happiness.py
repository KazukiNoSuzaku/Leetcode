# Author: Kaustav Ghosh
# Problem: Maximize Grid Happiness
# Approach: Filling the grid cell by cell in row-major order means a cell's only already-placed neighbours are the one directly left and the one directly above, so the entire relevant history is the last n cells; each holds one of three states, which packs into a single base-three number. The search is then over the cell index, that window, and how many of each personality remain, and because happiness changes are local the score of a placement can be charged immediately: the newcomer's own base value, adjusted for each occupied neighbour, plus the matching adjustment to that neighbour, so no adjacency is counted twice or missed. Memoising on the four state components collapses the exponential grid search to a few hundred thousand states.

from functools import lru_cache


class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        total_cells = m * n
        top_digit = 3 ** (n - 1)

        def adjust(state):
            # How one person's happiness moves per occupied neighbour.
            return -30 if state == 1 else 20

        @lru_cache(maxsize=None)
        def best(index, window, introverts, extroverts):
            if index == total_cells or (introverts == 0 and extroverts == 0):
                return 0
            column = index % n
            above = window // top_digit
            left = window % 3 if column else 0
            trimmed = (window % top_digit) * 3

            # Leave this cell empty.
            result = best(index + 1, trimmed, introverts, extroverts)

            for state, remaining in ((1, introverts), (2, extroverts)):
                if not remaining:
                    continue
                gained = 120 if state == 1 else 40
                for neighbour in (above, left):
                    if neighbour:
                        gained += adjust(state) + adjust(neighbour)
                following = best(index + 1, trimmed + state,
                                 introverts - (state == 1), extroverts - (state == 2))
                if gained + following > result:
                    result = gained + following
            return result

        answer = best(0, 0, introvertsCount, extrovertsCount)
        best.cache_clear()
        return answer
