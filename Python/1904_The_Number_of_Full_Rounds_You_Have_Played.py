# Author: Kaustav Ghosh
# Problem: The Number of Full Rounds You Have Played
# Approach: Convert both times to minutes (add a day if logout wraps past midnight). A full round fits between a 15-minute mark at or after login and one at or before logout, so round the start up and the end down to multiples of 15 and count the rounds between

class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        def to_min(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)

        start = to_min(loginTime)
        end = to_min(logoutTime)
        if end < start:
            end += 24 * 60

        first = -(-start // 15)   # ceil to next 15-min mark (in units of rounds)
        last = end // 15          # floor to previous 15-min mark
        return max(0, last - first)
