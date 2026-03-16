# Return the smaller angle (in degrees) between the hour and minute hands at h:m.

# Author: Kaustav Ghosh

class Solution(object):
    def angleClock(self, hour, minutes):
        minute_angle = minutes * 6.0
        hour_angle = (hour % 12) * 30.0 + minutes * 0.5
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
