# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

import bisect

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        # Longest non-decreasing subsequence ending at each position
        tails = []
        ans = []
        for obs in obstacles:
            pos = bisect.bisect_right(tails, obs)
            if pos == len(tails):
                tails.append(obs)
            else:
                tails[pos] = obs
            ans.append(pos + 1)
        return ans
