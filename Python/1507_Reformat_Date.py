# Convert a date string from "Day Month Year" format to "YYYY-MM-DD" format.

# Author: Kaustav Ghosh

class Solution(object):
    def reformatDate(self, date):
        months = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06",
                  "Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
        parts = date.split()
        day = parts[0][:-2].zfill(2)
        month = months[parts[1]]
        year = parts[2]
        return "{}-{}-{}".format(year, month, day)
