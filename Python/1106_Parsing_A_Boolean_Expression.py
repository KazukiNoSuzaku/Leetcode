# Author: Kaustav Ghosh
# 1106. Parsing A Boolean Expression
# https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        self.i = 0

        def parse():
            c = expression[self.i]
            self.i += 1
            if c == 't':
                return True
            if c == 'f':
                return False
            if c == '!':
                self.i += 1  # skip '('
                val = not parse()
                self.i += 1  # skip ')'
                return val
            if c == '&':
                self.i += 1  # skip '('
                result = True
                first = True
                while expression[self.i] != ')':
                    if not first:
                        self.i += 1  # skip ','
                    result = parse() and result
                    first = False
                self.i += 1  # skip ')'
                return result
            if c == '|':
                self.i += 1  # skip '('
                result = False
                first = True
                while expression[self.i] != ')':
                    if not first:
                        self.i += 1  # skip ','
                    result = parse() or result
                    first = False
                self.i += 1  # skip ')'
                return result

        return parse()
