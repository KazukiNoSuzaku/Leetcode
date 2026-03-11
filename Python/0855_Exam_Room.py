# Design an exam room where students sit maximizing distance to nearest person.

# Author: Kaustav Ghosh

import bisect

class ExamRoom(object):
    def __init__(self, n):
        self.n = n
        self.seats = []

    def seat(self):
        if not self.seats:
            bisect.insort(self.seats, 0)
            return 0
        max_dist = self.seats[0]
        idx = 0
        for i in range(1, len(self.seats)):
            d = (self.seats[i] - self.seats[i-1]) // 2
            if d > max_dist:
                max_dist = d
                idx = i
        last_dist = self.n - 1 - self.seats[-1]
        if last_dist > max_dist:
            seat = self.n - 1
        else:
            seat = self.seats[idx-1] + max_dist if idx > 0 else 0
        bisect.insort(self.seats, seat)
        return seat

    def leave(self, p):
        self.seats.remove(p)
