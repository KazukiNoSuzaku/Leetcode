# Evaluate a Lisp-like expression supporting let, add, mult, and variables.

# Author: Kaustav Ghosh

class Solution(object):
    def evaluate(self, expression):
        def parse(expr, scope):
            if expr[0] != '(':
                if expr.lstrip('-').isdigit(): return int(expr)
                return scope[expr]
            inner = expr[1:-1]
            if inner.startswith('let'):
                tokens = split(inner[4:])
                local = dict(scope)
                i = 0
                while i < len(tokens) - 1:
                    local[tokens[i]] = parse(tokens[i+1], local)
                    i += 2
                return parse(tokens[-1], local)
            elif inner.startswith('add'):
                tokens = split(inner[4:])
                return parse(tokens[0], scope) + parse(tokens[1], scope)
            else:
                tokens = split(inner[5:])
                return parse(tokens[0], scope) * parse(tokens[1], scope)
        def split(s):
            result, depth, cur = [], 0, ''
            for c in s:
                if c == '(': depth += 1
                if c == ')': depth -= 1
                if c == ' ' and depth == 0:
                    result.append(cur); cur = ''
                else: cur += c
            if cur: result.append(cur)
            return result
        return parse(expression, {})
