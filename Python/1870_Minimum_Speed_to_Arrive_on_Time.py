# Author: Kaustav Ghosh
# Problem: Minimum Speed to Arrive on Time
# Approach: Raising the speed can never make the journey longer, so whether a speed arrives in time is a monotone property and the smallest workable speed is found by binary search. The travel time is the only delicate part: every leg but the last is rounded up to a whole hour while the final leg is not, and the deadline carries two decimal places, so comparing in floating point risks tipping an exact deadline the wrong way. Multiplying through by the speed and by a hundred turns the test into integer arithmetic, which settles those boundary cases exactly. The search tops out at ten million because the tightest possible case, one leg of a hundred thousand with a hundredth of an hour, needs exactly that.

class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        hundredths = int(round(hour * 100))
        last = dist[-1]
        earlier = dist[:-1]

        def arrives(speed):
            whole = 0
            for leg in earlier:
                whole += -(-leg // speed)
            # whole + last / speed <= hour, cleared of both the division and the decimal
            return (whole * speed + last) * 100 <= hundredths * speed

        low, high = 1, 10 ** 7
        if not arrives(high):
            return -1
        while low < high:
            middle = (low + high) // 2
            if arrives(middle):
                high = middle
            else:
                low = middle + 1
        return low
