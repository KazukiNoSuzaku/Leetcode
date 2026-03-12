# Author: Kaustav Ghosh
# 1109. Corporate Flight Bookings
# https://leetcode.com/problems/corporate-flight-bookings/

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats
        result = []
        cur = 0
        for i in range(n):
            cur += diff[i]
            result.append(cur)
        return result
