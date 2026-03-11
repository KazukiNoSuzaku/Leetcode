# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
# You want to use all the matchsticks to make one square. Return true if you can make this square.

# Author: Kaustav Ghosh

class Solution(object):
    def makesquare(self, matchsticks):
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False
        buckets = [0] * 4

        def dfs(idx):
            if idx == len(matchsticks):
                return buckets[0] == buckets[1] == buckets[2] == side
            seen = set()
            for i in range(4):
                if buckets[i] + matchsticks[idx] <= side and buckets[i] not in seen:
                    seen.add(buckets[i])
                    buckets[i] += matchsticks[idx]
                    if dfs(idx + 1):
                        return True
                    buckets[i] -= matchsticks[idx]
            return False

        return dfs(0)
