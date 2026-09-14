# Author: Kaustav Ghosh
# Problem: The Latest Time to Catch a Bus
# Approach: Sort buses and passengers and simulate boarding, filling each bus in arrival order up to capacity. On the last bus, the best candidate is its departure time if a seat is left, otherwise the arrival time of the last passenger who boarded; since arrival times must be unique, step back one minute while the candidate collides with a boarded passenger

class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        buses = sorted(buses)
        passengers = sorted(passengers)
        j = 0
        count = 0
        for bus in buses:
            count = 0
            while count < capacity and j < len(passengers) and passengers[j] <= bus:
                j += 1
                count += 1
        ans = buses[-1] if count < capacity else passengers[j - 1]
        k = j - 1
        while k >= 0 and passengers[k] == ans:
            ans -= 1
            k -= 1
        return ans
