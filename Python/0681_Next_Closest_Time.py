# Given a time string, find the next closest time using same digits.

# Author: Kaustav Ghosh

class Solution(object):
    def nextClosestTime(self, time):
        digits = sorted(set(time.replace(':', '')))
        h, m = int(time[:2]), int(time[3:])
        while True:
            m += 1
            if m == 60:
                m = 0
                h = (h + 1) % 24
            candidate = '%02d:%02d' % (h, m)
            if all(c in digits for c in candidate if c != ':'):
                return candidate
