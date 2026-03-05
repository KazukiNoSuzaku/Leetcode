# Given a string expression of numbers and operators, return all possible results from computing
# all the different possible ways to group numbers and operators.

# Example 1:
# Input: expression = "2-1-1"
# Output: [0,2]

# Example 2:
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]

# Constraints:
# 1 <= expression.length <= 20
# expression consists of digits and the operators '+', '-', and '*'.

# Author: Kaustav Ghosh

class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}
        def solve(expr):
            if expr in memo:
                return memo[expr]
            if expr.isdigit() or (len(expr) == 2 and expr[0] == '-'):
                return [int(expr)]
            res = []
            for i, c in enumerate(expr):
                if c in '+-*':
                    for l in solve(expr[:i]):
                        for r in solve(expr[i+1:]):
                            if c == '+': res.append(l + r)
                            elif c == '-': res.append(l - r)
                            else: res.append(l * r)
            memo[expr] = res
            return res
        return solve(expression)
