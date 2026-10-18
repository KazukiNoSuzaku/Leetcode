# Author: Kaustav Ghosh
# Problem: Slowest Key
# Approach: A key's duration is its release time minus the previous release time, with the first press measured from zero, so one pass computes every duration without storing them. The tie-break asks for the lexicographically largest key among equal durations, which is handled by replacing the current answer only when a strictly longer duration appears or when an equal duration belongs to a later character.

class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        longest = releaseTimes[0]
        answer = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            key = keysPressed[i]
            if duration > longest or (duration == longest and key > answer):
                longest = duration
                answer = key
        return answer
