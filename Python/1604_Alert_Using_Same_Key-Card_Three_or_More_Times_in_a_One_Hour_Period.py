# Author: Kaustav Ghosh
# Problem: Alert Using Same Key-Card Three or More Times in a One Hour Period
# Approach: Group swipe times per worker in minutes, sort, and flag anyone whose 3rd swipe lands within 60 minutes of the 1st in some window

from collections import defaultdict

class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        times = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            hh, mm = t.split(':')
            times[name].append(int(hh) * 60 + int(mm))

        alerts = []
        for name, mins in times.items():
            mins.sort()
            if any(mins[i + 2] - mins[i] <= 60 for i in range(len(mins) - 2)):
                alerts.append(name)
        return sorted(alerts)
