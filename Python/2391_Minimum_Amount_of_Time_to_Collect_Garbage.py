# Author: Kaustav Ghosh
# Problem: Minimum Amount of Time to Collect Garbage
# Approach: Picking up each unit of garbage takes one minute whichever truck does it, so start from the total length of all the strings. Each truck only needs to drive as far as the last house holding its type, so add the prefix travel time up to that house for every type that appears

class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        prefix = [0]
        for t in travel:
            prefix.append(prefix[-1] + t)
        last = {}
        for i, house in enumerate(garbage):
            for kind in house:
                last[kind] = i
        return sum(len(house) for house in garbage) + sum(prefix[i] for i in last.values())
