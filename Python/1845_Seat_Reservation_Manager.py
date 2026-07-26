# Author: Kaustav Ghosh
# Problem: Seat Reservation Manager
# Approach: Track the next never-reserved seat with a counter, and hold explicitly unreserved seats in a min-heap so reserve() always returns the smallest available

import heapq

class SeatManager(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.next_seat = 1          # smallest seat never handed out yet
        self.freed = []             # min-heap of returned seats

    def reserve(self):
        """
        :rtype: int
        """
        if self.freed:
            return heapq.heappop(self.freed)
        seat = self.next_seat
        self.next_seat += 1
        return seat

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.freed, seatNumber)
