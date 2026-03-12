# Author: Kaustav Ghosh
# 1118. Number of Days in a Month
# https://leetcode.com/problems/number-of-days-in-a-month/

class Solution(object):
    def numberOfDays(self, year, month):
        """
        :type year: int
        :type month: int
        :rtype: int
        """
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
        return days[month]
