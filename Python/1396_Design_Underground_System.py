# Author: Kaustav Ghosh
# Problem: Design Underground System
# Approach: Track check-in times and compute running averages

class Solution(object):
    pass

class UndergroundSystem(object):

    def __init__(self):
        self.checkins = {}  # id -> (station, time)
        self.travel = {}    # (start, end) -> [total_time, count]

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_station, start_time = self.checkins.pop(id)
        key = (start_station, stationName)
        if key not in self.travel:
            self.travel[key] = [0, 0]
        self.travel[key][0] += t - start_time
        self.travel[key][1] += 1

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        total, count = self.travel[(startStation, endStation)]
        return float(total) / count
