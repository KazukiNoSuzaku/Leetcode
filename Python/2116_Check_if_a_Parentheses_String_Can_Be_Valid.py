# Author: Kaustav Ghosh
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 == 1:
            return False

        # Forward pass: ensure we never have too many closing parens
        balance = 0
        for i in range(n):
            if locked[i] == '0' or s[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        # Backward pass: ensure we never have too many opening parens
        balance = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        return True
