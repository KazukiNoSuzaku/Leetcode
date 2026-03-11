# A complex number can be represented as a string on the form "real+imaginaryi".
# Given two complex number strings num1 and num2, return a string of the complex product.

# Author: Kaustav Ghosh

class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        def parse(s):
            a, b = s[:-1].split('+')
            return int(a), int(b)
        a, b = parse(num1)
        c, d = parse(num2)
        return '%d+%di' % (a*c - b*d, a*d + b*c)
