# Book events; allow double booking but not triple booking.

# Author: Kaustav Ghosh

class MyCalendarTwo(object):
    def __init__(self):
        self.singles = []
        self.doubles = []

    def book(self, start, end):
        for s, e in self.doubles:
            if start < e and end > s: return False
        for s, e in self.singles:
            if start < e and end > s:
                self.doubles.append((max(start, s), min(end, e)))
        self.singles.append((start, end))
        return True
