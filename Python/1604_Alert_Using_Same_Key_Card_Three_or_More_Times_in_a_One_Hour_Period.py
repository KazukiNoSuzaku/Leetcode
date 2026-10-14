# Author: Kaustav Ghosh
# Problem: Alert Using Same Key-Card Three or More Times in a One Hour Period
# Approach: The uses are given in no particular order and the window is per person, so I bucket the times by name and convert each to minutes past midnight, which makes the one-hour test plain arithmetic rather than clock handling. Within a sorted list of times, three uses within an hour exist precisely when some time and the one two places later differ by at most sixty, because any tighter triple would also satisfy that for its own first element, so one scan over each person's sorted times decides it.

from collections import defaultdict


class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        uses = defaultdict(list)
        for name, stamp in zip(keyName, keyTime):
            hours, minutes = stamp.split(':')
            uses[name].append(int(hours) * 60 + int(minutes))

        flagged = []
        for name, times in uses.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    flagged.append(name)
                    break
        flagged.sort()
        return flagged
