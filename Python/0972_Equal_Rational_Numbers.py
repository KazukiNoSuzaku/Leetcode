# Two rational number strings may have repeating decimals.
# Return true if they represent the same number.

# Author: Kaustav Ghosh

from fractions import Fraction

class Solution(object):
    def isRationalEqual(self, s, t):
        def toFrac(s):
            if '(' not in s:
                return Fraction(s)
            i = s.index('(')
            base = Fraction(s[:i]) if s[:i] != '' and s[:i] != '-' else Fraction(0)
            non_rep = s[:i].split('.')
            rep = s[i+1:-1]
            rep_len = len(rep)
            non_rep_dec = len(non_rep[1]) if '.' in s[:i] else 0
            # value = base + rep/(9...9 * 10^non_rep_dec)
            rep_val = Fraction(int(rep), int('9' * rep_len) * (10 ** non_rep_dec))
            return Fraction(s[:i]) + rep_val if s[:i] else rep_val
        return toFrac(s) == toFrac(t)
