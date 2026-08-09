# Author: Kaustav Ghosh
# Problem: Find the Longest Valid Obstacle Course at Each Position
# Approach: For each index find the longest non-decreasing subsequence ending there via patience sorting. bisect_right keeps the sequence non-decreasing (equal heights allowed); the insertion index plus one is the answer for that position

import bisect

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        tails = []
        ans = []
        for x in obstacles:
            idx = bisect.bisect_right(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
            ans.append(idx + 1)
        return ans
