# Author: Kaustav Ghosh
# Problem: Maximum Nesting Depth of the Parentheses
# Approach: The input is guaranteed to be a valid parenthesis string, so there is no need to validate anything or keep a stack of the brackets themselves: the nesting depth at any point is simply how many openings have not yet been closed, which one counter tracks, and the answer is the largest value that counter ever reaches. Everything that is not a bracket can be ignored outright.

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        deepest = 0
        for ch in s:
            if ch == '(':
                depth += 1
                if depth > deepest:
                    deepest = depth
            elif ch == ')':
                depth -= 1
        return deepest
