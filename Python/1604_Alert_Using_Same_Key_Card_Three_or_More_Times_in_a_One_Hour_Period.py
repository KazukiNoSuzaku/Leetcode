# Author: Kaustav Ghosh
# Problem: 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
# Approach: Group by name, sort times, sliding window of size >= 3

from collections import defaultdict

class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        times = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            h, m = int(time[:2]), int(time[3:])
            times[name].append(h * 60 + m)

        result = []
        for name, ts in times.items():
            ts.sort()
            for i in range(2, len(ts)):
                if ts[i] - ts[i - 2] <= 60:
                    result.append(name)
                    break

        return sorted(result)
