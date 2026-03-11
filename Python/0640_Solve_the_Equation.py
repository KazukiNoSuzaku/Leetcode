# Solve a linear equation like "x+5-3+x=6+x-2" and return the solution.

# Author: Kaustav Ghosh

class Solution(object):
    def solveEquation(self, equation):
        def parse(s):
            coef = val = 0
            i = 0
            sign = 1
            while i < len(s):
                if s[i] == '+':
                    sign = 1; i += 1
                elif s[i] == '-':
                    sign = -1; i += 1
                elif s[i] == 'x':
                    coef += sign; i += 1
                else:
                    j = i
                    while j < len(s) and s[j].isdigit(): j += 1
                    num = int(s[i:j])
                    if j < len(s) and s[j] == 'x':
                        coef += sign * num; j += 1
                    else:
                        val += sign * num
                    i = j
            return coef, val
        left, right = equation.split('=')
        lc, lv = parse(left)
        rc, rv = parse(right)
        dc, dv = lc - rc, rv - lv
        if dc == 0:
            return "Infinite solutions" if dv == 0 else "No solution"
        return "x=%d" % (dv // dc)
