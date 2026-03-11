# Given integers a and b, return any string with exactly a 'a's and b 'b's
# such that "aaa" and "bbb" never appear.

# Author: Kaustav Ghosh

class Solution(object):
    def strWithout3a3b(self, a, b):
        res = []
        while a > 0 or b > 0:
            if a > b:
                res.append('aa' if a > 1 else 'a')
                a -= 2 if a > 1 else 1
                if b > 0:
                    res.append('b')
                    b -= 1
            elif b > a:
                res.append('bb' if b > 1 else 'b')
                b -= 2 if b > 1 else 1
                if a > 0:
                    res.append('a')
                    a -= 1
            else:
                res.append('ab')
                a -= 1
                b -= 1
        return ''.join(res)
