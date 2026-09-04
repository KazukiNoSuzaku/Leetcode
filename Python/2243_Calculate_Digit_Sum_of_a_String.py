# Author: Kaustav Ghosh
# Problem: Calculate Digit Sum of a String
# Approach: While the string is longer than k, split it into consecutive groups of k characters (the last group may be shorter), replace each group with the string of its digit sum, and concatenate. Repeat until the length is at most k

class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                group = s[i:i + k]
                parts.append(str(sum(int(c) for c in group)))
            s = "".join(parts)
        return s
