# Author: Kaustav Ghosh
# https://leetcode.com/problems/slowest-key/

class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        max_dur = releaseTimes[0]
        result = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            dur = releaseTimes[i] - releaseTimes[i - 1]
            if dur > max_dur or (dur == max_dur and keysPressed[i] > result):
                max_dur = dur
                result = keysPressed[i]
        return result
