# Author: Kaustav Ghosh
# Problem: Reformat Date
# Approach: The three space-separated parts are fixed in shape, so strip the two-letter ordinal suffix from the day, look the month up in a table, and reassemble as YYYY-MM-DD with the day zero-padded

class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                  "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                  "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day, month, year = date.split()
        return "%s-%s-%02d" % (year, months[month], int(day[:-2]))
