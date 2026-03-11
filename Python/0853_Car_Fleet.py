# Count car fleets arriving at destination; faster cars behind slower merge.

# Author: Kaustav Ghosh

class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / float(s) for p, s in cars]
        fleets = 0
        max_time = 0
        for t in times:
            if t > max_time:
                fleets += 1
                max_time = t
        return fleets
