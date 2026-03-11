# Evaluate an expression with variables and return simplified polynomial form.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        lookup = dict(zip(evalvars, evalints))
        def make(val):
            poly = defaultdict(int)
            if isinstance(val, int):
                poly[()] = val
            else:
                poly[(val,)] = 1
            return poly
        def combine(a, b, op):
            res = defaultdict(int)
            if op == '+':
                for k, v in list(a.items()) + list(b.items()):
                    res[k] += v
            elif op == '-':
                for k, v in a.items(): res[k] += v
                for k, v in b.items(): res[k] -= v
            else:
                for k1, v1 in a.items():
                    for k2, v2 in b.items():
                        res[tuple(sorted(k1+k2))] += v1 * v2
            return {k: v for k, v in res.items() if v}
        def parse(tokens):
            stack = []
            op = '+'
            while tokens:
                t = tokens.pop()
                if t == '(':
                    val = parse(tokens)
                elif t == ')':
                    break
                elif t.lstrip('-').isdigit():
                    val = make(int(t))
                elif t in lookup:
                    val = make(lookup[t])
                elif t in '+-*':
                    op = t
                    continue
                else:
                    val = make(t)
                if op == '+': stack.append(val)
                elif op == '-': stack.append(combine(defaultdict(int), val, '-'))
                else: stack.append(combine(stack.pop(), val, '*'))
            res = defaultdict(int)
            for poly in stack:
                for k, v in poly.items(): res[k] += v
            return res
        tokens = expression.replace('(', '( ').replace(')', ' )').split()
        poly = parse(tokens[::-1])
        def fmt(k, v):
            parts = list(k) + [str(v)]
            return '*'.join(parts) if k else str(v)
        return [fmt(k, v) for k, v in sorted(poly.items(), key=lambda x: (-len(x[0]), x[0])) if v]
