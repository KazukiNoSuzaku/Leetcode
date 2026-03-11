# Return the maximum k-booking after each event is added.

# Author: Kaustav Ghosh

from collections import defaultdict

class MyCalendarThree(object):
    def __init__(self):
        self.diff = defaultdict(int)

    def book(self, start, end):
        self.diff[start] += 1
        self.diff[end] -= 1
        cur = res = 0
        for k in sorted(self.diff):
            cur += self.diff[k]
            res = max(res, cur)
        return res
