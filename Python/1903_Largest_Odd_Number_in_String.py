# Author: Kaustav Ghosh
# Problem: Largest Odd Number in String
# Approach: Any substring that is a prefix is at least as long as, and therefore at least as large as, any shorter one, so the biggest odd value is the longest prefix ending on an odd digit. Scanning backwards for the last odd digit finds that prefix immediately, and finding none means every digit is even and no odd substring exists at all.

class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for index in range(len(num) - 1, -1, -1):
            if int(num[index]) % 2:
                return num[:index + 1]
        return ""
