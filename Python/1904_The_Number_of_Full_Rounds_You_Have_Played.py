# Author: Kaustav Ghosh
# Problem: The Number of Full Rounds You Have Played
# Approach: Rounds sit on the quarter hours regardless of when the session runs, so converting both times to minutes turns the count into how many quarter-hour boundaries fit entirely inside the interval: the first usable round starts at the login time rounded up to a quarter, the last usable one ends at the logout time rounded down, and the count is the gap between those two in units of fifteen minutes. A logout earlier than the login means the session crossed midnight, so a day is added to it, and the result is floored at zero for a session too short to contain a single round.

class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        def minutes(stamp):
            return int(stamp[:2]) * 60 + int(stamp[3:])

        start, end = minutes(loginTime), minutes(logoutTime)
        if end < start:
            end += 24 * 60
        return max(0, end // 15 - -(-start // 15))
