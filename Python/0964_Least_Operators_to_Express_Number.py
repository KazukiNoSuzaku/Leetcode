# Given an integer x and a target t, express t using only x and +, -, *, /.
# Return the minimum number of operators needed (x itself counts as 0).

# Author: Kaustav Ghosh

class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        # pos[i] = min ops to form target using x^i terms, with positive remainder
        # neg[i] = min ops to form target using x^i terms, with negative
        pos, neg, i = 0, 0, 0
        while target:
            t = target % x
            target //= x
            if i == 0:
                # cost of t copies of x^0 = x/x = 1 uses 2*t operators (each pair)
                pos = t * 2
                neg = (x - t) * 2
            else:
                pos, neg = min(t * (i+1) + pos, (t+1) * (i+1) + neg), \
                           min((x-t) * (i+1) + pos, (x-t-1) * (i+1) + neg)
            i += 1
        return min(pos, i + neg) - 1
