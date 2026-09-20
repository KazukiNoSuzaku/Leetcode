# Author: Kaustav Ghosh
# Problem: Optimal Partition of String
# Approach: Extend the current piece until a letter repeats inside it, then start a new piece. Cutting only when forced is optimal, because any valid partition must also cut somewhere within each stretch this one keeps whole

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        parts = 1
        for ch in s:
            if ch in seen:
                parts += 1
                seen = set()
            seen.add(ch)
        return parts
