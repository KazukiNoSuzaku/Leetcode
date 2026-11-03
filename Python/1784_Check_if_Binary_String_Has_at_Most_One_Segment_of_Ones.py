# Author: Kaustav Ghosh
# Problem: Check if Binary String Has at Most One Segment of Ones
# Approach: Splitting the string on zeros leaves one piece per run of ones, plus empty pieces wherever zeros sat next to each other or at an end. Discarding the empty pieces therefore counts the segments of ones directly, which only has to be at most one.

class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len([run for run in s.split("0") if run]) <= 1
