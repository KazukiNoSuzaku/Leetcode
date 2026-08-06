# Author: Kaustav Ghosh
# Problem: Maximum Compatibility Score Sum
# Approach: Precompute each student-mentor compatibility (matching answers). With at most 8 students, DP over a bitmask of assigned mentors: the number of set bits is the next student to assign, so extend by any free mentor and maximize

class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        m = len(students)
        n = len(students[0])
        score = [[sum(a == b for a, b in zip(students[i], mentors[j])) for j in range(m)] for i in range(m)]

        dp = [-1] * (1 << m)
        dp[0] = 0
        for mask in range(1 << m):
            if dp[mask] < 0:
                continue
            i = bin(mask).count('1')      # next student to assign
            if i == m:
                continue
            for j in range(m):
                if not (mask >> j) & 1:
                    nxt = mask | (1 << j)
                    cand = dp[mask] + score[i][j]
                    if cand > dp[nxt]:
                        dp[nxt] = cand
        return dp[(1 << m) - 1]
