# Compute the "clumsy factorial" of n: apply *, /, +, - cyclically left to right.

# Author: Kaustav Ghosh

class Solution(object):
    def clumsy(self, n):
        stack = [n]
        n -= 1
        op = 0  # 0=*, 1=/, 2=+, 3=-
        while n > 0:
            if op == 0:
                stack[-1] *= n
            elif op == 1:
                stack[-1] = int(stack[-1] / n)
            elif op == 2:
                stack.append(n)
            else:
                stack.append(-n)
            op = (op + 1) % 4
            n -= 1
        return sum(stack)
