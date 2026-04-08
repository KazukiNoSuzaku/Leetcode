# Author: Kaustav Ghosh
# Problem: 2232. Minimize Result by Adding Parentheses to Expression
# URL: https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/
# Difficulty: Medium
#
# Approach:
# Try all possible positions for the opening parenthesis (before any digit of
# the first number) and the closing parenthesis (after any digit of the second
# number). The part before '(' multiplies the sum inside, and the part after
# ')' multiplies the sum inside. Pick the placement that minimizes the result.

class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        plus = expression.index('+')
        left = expression[:plus]
        right = expression[plus + 1:]
        best_val = float('inf')
        best_expr = expression
        for i in range(len(left)):
            for j in range(1, len(right) + 1):
                prefix = int(left[:i]) if i > 0 else 1
                inside_left = int(left[i:])
                inside_right = int(right[:j])
                suffix = int(right[j:]) if j < len(right) else 1
                val = prefix * (inside_left + inside_right) * suffix
                if val < best_val:
                    best_val = val
                    best_expr = left[:i] + '(' + left[i:] + '+' + right[:j] + ')' + right[j:]
        return best_expr
