# Author: Kaustav Ghosh

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if int(s[i]) != i % 2:
                count += 1
        return min(count, len(s) - count)
