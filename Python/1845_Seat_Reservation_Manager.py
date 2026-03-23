# Author: Kaustav Ghosh
# Problem 1845: Seat Reservation Manager

import heapq

class SeatManager(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.available = list(range(1, n + 1))

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.available, seatNumber)
