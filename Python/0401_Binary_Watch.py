# A binary watch has 4 LEDs on the top to represent the hours (0-11) and
# 6 LEDs on the bottom to represent the minutes (0-59).
# Given an integer turnedOn which represents the number of LEDs that are currently on,
# return all possible times the watch could represent.

# Author: Kaustav Ghosh

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append('%d:%02d' % (h, m))
        return res
