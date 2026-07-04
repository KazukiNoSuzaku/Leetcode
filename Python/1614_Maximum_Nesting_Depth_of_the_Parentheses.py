# Author: Kaustav Ghosh
# Problem: Maximum Nesting Depth of the Parentheses
# Approach: Sweep left to right tracking open-paren depth, recording the peak

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        best = 0
        for c in s:
            if c == '(':
                depth += 1
                best = max(best, depth)
            elif c == ')':
                depth -= 1
        return best
