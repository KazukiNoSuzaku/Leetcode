# Author: Kaustav Ghosh
# Problem: Largest Odd Number in String
# Approach: The largest odd substring is the longest prefix ending in an odd digit, since a longer prefix is always a larger number. Scan from the right for the last odd digit

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""
