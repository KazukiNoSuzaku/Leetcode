# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-compatibility-score-sum/

class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        m = len(students)
        # Precompute compatibility scores
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(s == t for s, t in zip(students[i], mentors[j]))

        # Bitmask DP
        dp = [0] * (1 << m)
        for mask in range(1 << m):
            i = bin(mask).count('1')  # which student we're assigning
            if i >= m:
                continue
            for j in range(m):
                if not (mask & (1 << j)):
                    dp[mask | (1 << j)] = max(dp[mask | (1 << j)], dp[mask] + score[i][j])

        return dp[(1 << m) - 1]
