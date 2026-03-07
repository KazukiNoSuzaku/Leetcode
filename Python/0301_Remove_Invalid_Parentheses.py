# Given a string s that contains parentheses and letters, remove the minimum number of
# invalid parentheses to make the input string valid.
# Return a list of unique strings that are valid with the minimum number of removals.
# You may return the answer in any order.

# Example 1:
# Input: s = "()())()"
# Output: ["(())()", "()()()"]

# Example 2:
# Input: s = "(a)())()"
# Output: ["(a)()()", "(a())()"]

# Constraints:
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.

# Author: Kaustav Ghosh

class Solution(object):
    def removeInvalidParentheses(self, s):
        res = set()
        def count_invalid(t):
            left = right = 0
            for c in t:
                if c == '(':
                    left += 1
                elif c == ')':
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            return left, right

        def dfs(t, l, r):
            if l == 0 and r == 0:
                if count_invalid(t) == (0, 0):
                    res.add(t)
                return
            for i in range(len(t)):
                if t[i] not in '()':
                    continue
                if r > 0 and t[i] == ')':
                    dfs(t[:i] + t[i+1:], l, r - 1)
                elif l > 0 and t[i] == '(':
                    dfs(t[:i] + t[i+1:], l - 1, r)

        l, r = count_invalid(s)
        dfs(s, l, r)
        return list(res)
