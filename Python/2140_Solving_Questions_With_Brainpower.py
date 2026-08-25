# Author: Kaustav Ghosh
# Problem: Solving Questions With Brainpower
# Approach: DP from the last question. At each question either solve it (earn its points, then jump past the next brainpower questions) or skip to the next; take the better. dp[0] is the maximum points

class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            jump = i + brainpower + 1
            solve = points + (dp[jump] if jump <= n else 0)
            dp[i] = max(dp[i + 1], solve)
        return dp[0]
