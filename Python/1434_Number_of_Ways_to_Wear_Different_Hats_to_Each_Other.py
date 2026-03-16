# Author: Kaustav Ghosh
# Problem: Number of Ways to Wear Different Hats to Each Other
# Approach: Bitmask DP over people assigned hats (iterate over hats)

class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(hats)
        full_mask = (1 << n) - 1

        # Map hat -> list of people who like it
        hat_to_people = [[] for _ in range(41)]
        for person in range(n):
            for hat in hats[person]:
                hat_to_people[hat].append(person)

        dp = [0] * (full_mask + 1)
        dp[0] = 1

        for hat in range(1, 41):
            # Process in reverse to avoid using same hat twice
            for mask in range(full_mask, -1, -1):
                for person in hat_to_people[hat]:
                    if mask & (1 << person) == 0:
                        dp[mask | (1 << person)] = (dp[mask | (1 << person)] + dp[mask]) % MOD

        return dp[full_mask]
