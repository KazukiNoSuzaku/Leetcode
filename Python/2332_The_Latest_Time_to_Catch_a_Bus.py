# Author: Kaustav Ghosh
# 2332. The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
# Sort both, greedily assign passengers, find latest valid time not taken

class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        buses.sort()
        passengers.sort()
        taken = set(passengers)

        j = 0
        for i, bus in enumerate(buses):
            cap = capacity
            while j < len(passengers) and passengers[j] <= bus and cap > 0:
                j += 1
                cap -= 1

        # Try to board the last bus
        # If last bus has room, we can arrive at bus departure time (if not taken)
        # Otherwise we arrive just before the last boarded passenger
        ans = buses[-1]
        if cap == 0:
            # last slot was filled; back up from passengers[j-1]
            ans = passengers[j - 1] - 1

        while ans in taken:
            ans -= 1

        return ans
