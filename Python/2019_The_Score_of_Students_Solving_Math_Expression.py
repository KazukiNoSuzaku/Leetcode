# Author: Kaustav Ghosh
# Problem: The Score of Students Solving Math Expression
# Approach: The correct value uses normal precedence. Students apply operators in any order, so the achievable wrong answers are all results of every parenthesization, computed by interval DP over operands and pruned to <=1000 (answers never exceed that). Score 5 for the exact answer, 2 for any achievable value, else 0

class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        nums = [int(s[i]) for i in range(0, len(s), 2)]
        ops = [s[i] for i in range(1, len(s), 2)]
        m = len(nums)

        correct = eval(s)

        dp = [[set() for _ in range(m)] for _ in range(m)]
        for i in range(m):
            dp[i][i].add(nums[i])
        for length in range(2, m + 1):
            for i in range(0, m - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    op = ops[k]
                    for a in dp[i][k]:
                        for b in dp[k + 1][j]:
                            val = a + b if op == '+' else a * b
                            if val <= 1000:
                                dp[i][j].add(val)

        achievable = dp[0][m - 1]
        score = 0
        for ans in answers:
            if ans == correct:
                score += 5
            elif ans in achievable:
                score += 2
        return score
