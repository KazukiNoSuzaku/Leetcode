# Author: Kaustav Ghosh
# Problem: 2272. Substring With Largest Variance
# URL: https://leetcode.com/problems/substring-with-largest-variance/
# Difficulty: Hard
#
# Approach:
# For every pair of characters (a, b), apply Kadane's algorithm treating
# a as +1 and b as -1. Track whether b has appeared in the current window.
# If not, use a "can_extend" flag from a previous b to allow reset.

class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set(s)
        result = 0
        for a in chars:
            for b in chars:
                if a == b:
                    continue
                diff = 0
                has_b = False
                first_b = False
                for c in s:
                    if c == a:
                        diff += 1
                    elif c == b:
                        has_b = True
                        if first_b and diff >= 0:
                            first_b = False
                        elif diff - 1 < 0:
                            first_b = True
                            diff = -1
                        else:
                            diff -= 1
                    if has_b:
                        result = max(result, diff)
        return result
