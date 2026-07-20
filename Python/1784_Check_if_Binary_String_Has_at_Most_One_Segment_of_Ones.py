# Author: Kaustav Ghosh
# Problem: Check if Binary String Has at Most One Segment of Ones
# Approach: A second segment of ones is exactly a "01" appearing after the leading run, so the string is valid iff "01" never occurs

class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return '01' not in s
