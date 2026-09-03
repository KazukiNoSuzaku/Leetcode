# Author: Kaustav Ghosh
# Problem: Minimize Result by Adding Parentheses to Expression
# Approach: The single '+' splits the expression into num1 and num2. A parenthesis pair puts '(' before some digit of num1 and ')' after some digit of num2, giving value a * (b + c) * d where a/b are the split of num1 and c/d the split of num2 (empty outer parts count as 1). Try every split and keep the minimum

class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        plus = expression.index('+')
        num1 = expression[:plus]
        num2 = expression[plus + 1:]

        best_val = None
        best_str = None
        for i in range(len(num1)):
            for j in range(1, len(num2) + 1):
                a = num1[:i]
                b = num1[i:]
                c = num2[:j]
                d = num2[j:]
                left = int(a) if a else 1
                right = int(d) if d else 1
                val = left * (int(b) + int(c)) * right
                if best_val is None or val < best_val:
                    best_val = val
                    best_str = "{}({}+{}){}".format(a, b, c, d)
        return best_str
