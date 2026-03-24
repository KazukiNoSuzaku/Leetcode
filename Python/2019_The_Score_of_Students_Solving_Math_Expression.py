# Author: Kaustav Ghosh
# Problem 2019: The Score of Students Solving Math Expression

class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        # Parse numbers and operators
        nums = []
        ops = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                nums.append(int(s[i]))
            else:
                ops.append(s[i])
            i += 1

        n = len(nums)
        # dp[i][j] = set of possible results from nums[i..j] with any order of operations
        dp = [[set() for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].add(nums[i])

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    for a in dp[i][k]:
                        for b in dp[k + 1][j]:
                            if ops[k] == '+':
                                val = a + b
                            else:
                                val = a * b
                            if val <= 1000:
                                dp[i][j].add(val)

        # Compute correct answer (standard order of operations)
        # First handle multiplication
        stack = [nums[0]]
        for i in range(len(ops)):
            if ops[i] == '*':
                stack[-1] *= nums[i + 1]
            else:
                stack.append(nums[i + 1])
        correct = sum(stack)

        possible = dp[0][n - 1]
        score = 0
        for ans in answers:
            if ans == correct:
                score += 5
            elif ans in possible:
                score += 2
        return score
