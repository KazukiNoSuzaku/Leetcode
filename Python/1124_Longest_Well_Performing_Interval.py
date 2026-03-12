# Author: Kaustav Ghosh
# 1124. Longest Well-Performing Interval
# https://leetcode.com/problems/longest-well-performing-interval/

class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        score = 0
        seen = {}
        result = 0
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            if score > 0:
                result = i + 1
            else:
                if score - 1 in seen:
                    result = max(result, i - seen[score - 1])
            if score not in seen:
                seen[score] = i
        return result
