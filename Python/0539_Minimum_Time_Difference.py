# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes
# difference between any two time-points in the list.

# Author: Kaustav Ghosh

class Solution(object):
    def findMinDifference(self, timePoints):
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        minutes.append(minutes[0] + 1440)
        return min(minutes[i+1] - minutes[i] for i in range(len(minutes)-1))
