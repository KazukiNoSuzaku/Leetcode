# Author: Kaustav Ghosh
# Problem: Can You Eat Your Favorite Candy on Your Favorite Day?
# Approach: By day d you have eaten between d+1 and (d+1)*cap candies. Using prefix sums, the favorite type is reachable iff the greedy max gets past everything before it and the slow min has not already passed it

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
        for fav_type, fav_day, cap in queries:
            min_eaten = fav_day + 1              # at least one candy per day
            max_eaten = (fav_day + 1) * cap      # at most cap per day
            reaches = max_eaten > prefix[fav_type]
            not_past = min_eaten <= prefix[fav_type + 1]
            res.append(reaches and not_past)
        return res
