# Author: Kaustav Ghosh
# Problem: Maximum Number of People That Can Be Caught in Tag
# Approach: Each catcher can take one person within dist of them, so this is a matching between two sets of positions on a line where a pair is allowed when their positions are close enough; on a line that matching is solved greedily. Walking both sorted position lists together, I give the earliest catcher the earliest free person it can still reach: anyone too far to the left of that catcher is out of reach of every later catcher too and can be dropped, and if the earliest reachable person is too far right the catcher has nobody and is dropped. Matching the earliest reachable person is never worse than saving them for a later catcher, since a later catcher reaches everything to the right that this one does. Both pointers only move forward, so one pass over the array suffices.

class Solution(object):
    def catchMaximumAmountofPeople(self, team, dist):
        """
        :type team: List[int]
        :type dist: int
        :rtype: int
        """
        catchers = [index for index, flag in enumerate(team) if flag == 1]
        runners = [index for index, flag in enumerate(team) if flag == 0]

        caught = 0
        here = 0
        there = 0
        while here < len(catchers) and there < len(runners):
            if runners[there] < catchers[here] - dist:
                there += 1
            elif runners[there] > catchers[here] + dist:
                here += 1
            else:
                caught += 1
                here += 1
                there += 1
        return caught
