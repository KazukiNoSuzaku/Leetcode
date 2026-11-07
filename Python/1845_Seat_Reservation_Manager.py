# Author: Kaustav Ghosh
# Problem: Seat Reservation Manager
# Approach: Reserving always takes the smallest free seat, which is either one that was given back or, if none were, the next seat never handed out at all. Keeping only the returned seats in a heap and tracking the frontier of untouched seats with a counter means the structure starts empty instead of being loaded with all hundred thousand seats, and a seat above the frontier is never stored because its availability is implied. Each call is then a single heap operation or a counter bump.

class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.returned = []
        self.frontier = 1

    def reserve(self):
        """
        :rtype: int
        """
        from heapq import heappop

        if self.returned:
            return heappop(self.returned)
        seat = self.frontier
        self.frontier += 1
        return seat

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        from heapq import heappush

        heappush(self.returned, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
