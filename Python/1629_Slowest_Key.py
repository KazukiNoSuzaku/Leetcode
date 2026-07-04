# Author: Kaustav Ghosh
# Problem: Slowest Key
# Approach: Walk consecutive release times to get each press duration; keep the longest, breaking ties by the larger character

class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        best_key = keysPressed[0]
        best_dur = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            dur = releaseTimes[i] - releaseTimes[i - 1]
            if dur > best_dur or (dur == best_dur and keysPressed[i] > best_key):
                best_dur = dur
                best_key = keysPressed[i]
        return best_key
