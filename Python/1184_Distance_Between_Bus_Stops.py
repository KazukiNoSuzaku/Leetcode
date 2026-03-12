# Author: Kaustav Ghosh
# Min of clockwise vs counterclockwise distance

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        total = sum(distance)
        return min(clockwise, total - clockwise)
