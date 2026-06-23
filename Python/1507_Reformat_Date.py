# Author: Kaustav Ghosh
# Problem: Reformat Date
# Approach: Split parts, map month name to number, zero-pad day, reassemble as YYYY-MM-DD

class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        months = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
        }
        parts = date.split()
        day = parts[0][:-2].zfill(2)
        month = months[parts[1]]
        year = parts[2]
        return "{}-{}-{}".format(year, month, day)
