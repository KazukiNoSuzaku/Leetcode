# Author: Kaustav Ghosh
# Problem: Number of Days Between Two Dates
# Approach: Parse dates and compute absolute difference

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        def to_days(date):
            y, m, d = map(int, date.split('-'))
            # Days from year 0 using formula
            months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            days = 365 * y + d
            for i in range(1, m):
                days += months[i]
            if m <= 2:
                y -= 1
            days += y // 4 - y // 100 + y // 400
            return days

        return abs(to_days(date1) - to_days(date2))
