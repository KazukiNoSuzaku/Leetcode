# Our hero Teemo is attacking an enemy Ashe with poison attacks!
# When Teemo attacks Ashe, Ashe is poisoned for exactly duration seconds.
# Given timeSeries (times when Teemo attacks) and duration, return the total seconds Ashe is poisoned.

# Author: Kaustav Ghosh

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i+1] - timeSeries[i])
        total += duration
        return total
