# Design a calendar that can book events without overlapping.

# Author: Kaustav Ghosh

import bisect

class MyCalendar(object):
    def __init__(self):
        self.events = []

    def book(self, start, end):
        idx = bisect.bisect_right(self.events, (start, end))
        if (idx > 0 and self.events[idx-1][1] > start) or (idx < len(self.events) and self.events[idx][0] < end):
            return False
        bisect.insort(self.events, (start, end))
        return True
