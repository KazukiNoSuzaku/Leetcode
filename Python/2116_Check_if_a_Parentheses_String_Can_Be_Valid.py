# Author: Kaustav Ghosh
# Problem: Check if a Parentheses String Can Be Valid
# Approach: An odd length is impossible. Sweep left to right treating unlocked or '(' characters as potential opens; the running count must never go negative. Sweep right to left treating unlocked or ')' as potential closes with the same check. If both hold, a valid assignment exists

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

        balance = 0
        for i in range(n):
            if locked[i] == '0' or s[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        balance = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        return True
