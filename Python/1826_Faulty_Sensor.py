# Author: Kaustav Ghosh
# Problem: Faulty Sensor
# Approach: Up to the first disagreement both sensors recorded the same thing, so the defect has to be at that index: whichever sensor dropped a value from there on is shifted one place left relative to the other, except for its final slot which holds a replacement. So each sensor is tested by checking whether its tail, ignoring that last slot, lines up with the other sensor's readings shifted by one. If exactly one test passes that sensor is the faulty one, while both passing means the disagreement is only in the final slot and nothing distinguishes them, and neither passing means no single drop explains the data.

class Solution(object):
    def badSensor(self, sensor1, sensor2):
        """
        :type sensor1: List[int]
        :type sensor2: List[int]
        :rtype: int
        """
        n = len(sensor1)
        split = 0
        while split < n and sensor1[split] == sensor2[split]:
            split += 1
        if split == n:
            return -1

        first_dropped = sensor1[split:n - 1] == sensor2[split + 1:n]
        second_dropped = sensor2[split:n - 1] == sensor1[split + 1:n]
        if first_dropped and not second_dropped:
            return 1
        if second_dropped and not first_dropped:
            return 2
        return -1
