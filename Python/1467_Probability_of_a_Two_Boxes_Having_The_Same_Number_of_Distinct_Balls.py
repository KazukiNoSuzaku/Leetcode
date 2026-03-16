# Author: Kaustav Ghosh
# Problem: Probability of a Two Boxes Having The Same Number of Distinct Balls (Premium)
# Approach: DFS/backtracking with combinatorics to count valid distributions

from math import factorial

class Solution(object):
    def getProbability(self, balls):
        """
        :type balls: List[int]
        :rtype: float
        """
        n = sum(balls)
        half = n // 2
        k = len(balls)
        total = [0.0]
        valid = [0.0]

        def perm(counts):
            result = factorial(sum(counts))
            for c in counts:
                result //= factorial(c)
            return result

        def dfs(idx, left, right):
            left_sum = sum(left)
            right_sum = sum(right)
            if left_sum > half or right_sum > half:
                return
            if idx == k:
                if left_sum == right_sum:
                    ways = perm(left) * perm(right)
                    total[0] += ways
                    left_colors = sum(1 for x in left if x > 0)
                    right_colors = sum(1 for x in right if x > 0)
                    if left_colors == right_colors:
                        valid[0] += ways
                return
            for i in range(balls[idx] + 1):
                left[idx] = i
                right[idx] = balls[idx] - i
                dfs(idx + 1, left, right)
            left[idx] = 0
            right[idx] = 0

        left = [0] * k
        right = [0] * k
        dfs(0, left, right)
        return valid[0] / total[0]
