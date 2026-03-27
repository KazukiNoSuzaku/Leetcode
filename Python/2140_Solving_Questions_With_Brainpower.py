# Author: Kaustav Ghosh
# https://leetcode.com/problems/solving-questions-with-brainpower/

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
            nxt = i + brainpower + 1
            take = points + (dp[nxt] if nxt < n else 0)
            skip = dp[i + 1]
            dp[i] = max(take, skip)
        return dp[0]
