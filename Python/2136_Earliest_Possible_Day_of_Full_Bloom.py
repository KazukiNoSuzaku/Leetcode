# Author: Kaustav Ghosh
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        # Sort by grow time descending: plant the slowest growers first
        order = sorted(range(len(plantTime)), key=lambda i: -growTime[i])
        result = 0
        current_day = 0
        for i in order:
            current_day += plantTime[i]
            result = max(result, current_day + growTime[i])
        return result
