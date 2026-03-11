# Given courses with duration and deadline, find max number of courses you can take.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        heap = []
        time = 0
        for dur, deadline in courses:
            heapq.heappush(heap, -dur)
            time += dur
            if time > deadline:
                time += heapq.heappop(heap)  # pop largest (negative)
        return len(heap)
