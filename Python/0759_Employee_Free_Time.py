# Find common free time intervals among all employees.

# Author: Kaustav Ghosh

class Solution(object):
    def employeeFreeTime(self, schedule):
        intervals = sorted([iv for emp in schedule for iv in emp], key=lambda x: x.start)
        res = []
        end = intervals[0].end
        for iv in intervals[1:]:
            if iv.start > end:
                from collections import namedtuple
                Interval = type(iv)
                res.append(Interval(end, iv.start))
            end = max(end, iv.end)
        return res
