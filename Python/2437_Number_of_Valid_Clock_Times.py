# Author: Kaustav Ghosh
# Problem: Number of Valid Clock Times
# Approach: Hours and minutes are independent, so count how many of the 24 hours and how many of the 60 minutes match the given pattern, where a '?' matches any digit, and multiply the two counts

class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        def matches(pattern, limit):
            return sum(1 for value in range(limit)
                       if (pattern[0] == '?' or int(pattern[0]) == value // 10)
                       and (pattern[1] == '?' or int(pattern[1]) == value % 10))

        return matches(time[:2], 24) * matches(time[3:], 60)
