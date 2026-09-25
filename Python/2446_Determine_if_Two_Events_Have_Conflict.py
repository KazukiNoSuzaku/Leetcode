# Author: Kaustav Ghosh
# Problem: Determine if Two Events Have Conflict
# Approach: Times are zero-padded HH:MM, so they compare correctly as plain strings. Two intervals overlap exactly when the later start is not after the earlier end

class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])
