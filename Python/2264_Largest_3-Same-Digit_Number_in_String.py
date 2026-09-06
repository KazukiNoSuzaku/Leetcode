# Author: Kaustav Ghosh
# Problem: Largest 3-Same-Digit Number in String
# Approach: Scan every window of three consecutive characters; those made of one repeated digit are "good". Track the largest such window (comparing strings works since all are length 3). Return "" if none exists

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                window = num[i:i + 3]
                if window > best:
                    best = window
        return best
