# Author: Kaustav Ghosh
# Problem: Faulty Sensor (Premium)
# Approach: Find the first mismatch; a dropped value shifts everything after it, so test whether each sensor's tail (shifted by one) matches the other. If exactly one matches it is the good one, else ambiguous

class Solution(object):
    def badSensor(self, sensor1, sensor2):
        """
        :type sensor1: List[int]
        :type sensor2: List[int]
        :rtype: int
        """
        n = len(sensor1)
        i = 0
        while i < n and sensor1[i] == sensor2[i]:
            i += 1
        if i == n:
            return -1  # identical, cannot tell

        # If sensor1 dropped a value, its tail (minus the random last) matches sensor2 shifted
        s1_defective = sensor1[i:n - 1] == sensor2[i + 1:n]
        s2_defective = sensor2[i:n - 1] == sensor1[i + 1:n]

        if s1_defective and not s2_defective:
            return 1
        if s2_defective and not s1_defective:
            return 2
        return -1
