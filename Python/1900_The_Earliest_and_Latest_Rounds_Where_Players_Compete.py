# Author: Kaustav Ghosh
# Problem: The Earliest and Latest Rounds Where Players Compete
# Approach: Which particular players survive a round never matters, only how many players remain and where the two favourites sit among them, so the state is that triple and the recursion is memoised over it. The row is symmetric, so a configuration whose two positions sit past the midpoint is mirrored onto its reflection first, which halves the states and lets a single case handle the rest. From a state, the choices are how many of the players before the first favourite advance and how many of those between the two advance; everything else is forced, because the favourites beat anyone they meet. The two meet immediately exactly when their positions sum to one more than the row length, which is the base case, and otherwise each branch's answer is one round later than the subproblem it leads to.

class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def rounds(players, first, second):
            if first + second == players + 1:
                return 1, 1
            if first + second > players + 1:
                first, second = players + 1 - second, players + 1 - first
            survivors = (players + 1) // 2
            earliest, latest = players, 0
            if second * 2 <= players + 1:
                # Both favourites are in the front half of the row.
                for ahead in range(first):
                    for between in range(second - first):
                        e, l = rounds(survivors, ahead + 1, ahead + between + 2)
                        earliest = min(earliest, e)
                        latest = max(latest, l)
            else:
                # The second favourite is past the middle, so count from its mirror.
                mirrored = players + 1 - second
                middle = (players - 2 * mirrored + 1) // 2
                for ahead in range(first):
                    for between in range(mirrored - first):
                        e, l = rounds(survivors, ahead + 1,
                                      ahead + between + middle + 2)
                        earliest = min(earliest, e)
                        latest = max(latest, l)
            return earliest + 1, latest + 1

        earliest, latest = rounds(n, firstPlayer, secondPlayer)
        return [earliest, latest]
