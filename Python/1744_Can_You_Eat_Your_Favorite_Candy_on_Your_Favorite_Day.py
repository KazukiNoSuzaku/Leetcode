# Author: Kaustav Ghosh

class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prefix = [0]
        for c in candiesCount:
            prefix.append(prefix[-1] + c)
        res = []
        for fav_type, fav_day, daily_cap in queries:
            # Minimum candies eaten by fav_day: 1 per day = fav_day + 1
            # Maximum candies eaten by fav_day: daily_cap per day = (fav_day + 1) * daily_cap
            min_eaten = fav_day + 1
            max_eaten = (fav_day + 1) * daily_cap
            # Candies of fav_type are in range (prefix[fav_type], prefix[fav_type+1]]
            # We can eat fav_type candy if ranges overlap
            can = not (min_eaten > prefix[fav_type + 1] or max_eaten <= prefix[fav_type])
            res.append(can)
        return res
