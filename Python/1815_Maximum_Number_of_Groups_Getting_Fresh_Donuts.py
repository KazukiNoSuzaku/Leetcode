# Author: Kaustav Ghosh

class Solution(object):
    def maxHappyGroups(self, batchSize, groups):
        """
        :type batchSize: int
        :type groups: List[int]
        :rtype: int
        """
        from collections import Counter
        remainders = [g % batchSize for g in groups]
        cnt = Counter(remainders)
        happy = cnt.get(0, 0)
        cnt[0] = 0
        # Pair up complementary remainders
        for i in range(1, batchSize // 2 + 1):
            j = batchSize - i
            if i == j:
                pairs = cnt.get(i, 0) // 2
                happy += pairs
                cnt[i] = cnt.get(i, 0) - 2 * pairs
            else:
                pairs = min(cnt.get(i, 0), cnt.get(j, 0))
                happy += pairs
                cnt[i] = cnt.get(i, 0) - pairs
                cnt[j] = cnt.get(j, 0) - pairs
        # DP with remaining groups
        remaining = tuple(cnt.get(i, 0) for i in range(batchSize))
        memo = {}

        def dp(state, left_over):
            if state in memo:
                return memo[state]
            res = 0
            for i in range(1, batchSize):
                if state[i] > 0:
                    new_state = list(state)
                    new_state[i] -= 1
                    new_state = tuple(new_state)
                    bonus = 1 if left_over == 0 else 0
                    res = max(res, bonus + dp(new_state, (left_over + i) % batchSize))
            memo[state] = res
            return res

        return happy + dp(remaining, 0)
