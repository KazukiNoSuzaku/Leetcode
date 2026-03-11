# A frog is crossing a river. The river is divided into some number of units, and at
# each unit there may or may not exist a stone. The frog can jump on a stone, but it
# must not jump into the water. Given a list of stones positions, determine if the frog
# can cross the river by landing on the last stone. The first jump must be 1 unit.

# Author: Kaustav Ghosh

class Solution(object):
    def canCross(self, stones):
        stone_set = set(stones)
        dp = {s: set() for s in stones}
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                for jump in [k - 1, k, k + 1]:
                    if jump > 0 and stone + jump in stone_set:
                        dp[stone + jump].add(jump)
        return bool(dp[stones[-1]])
