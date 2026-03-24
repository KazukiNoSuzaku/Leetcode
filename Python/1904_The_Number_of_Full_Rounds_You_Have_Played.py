# Author: Kaustav Ghosh
# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        login = int(loginTime[:2]) * 60 + int(loginTime[3:])
        logout = int(logoutTime[:2]) * 60 + int(logoutTime[3:])
        if logout < login:
            logout += 24 * 60
        # Round login up to next multiple of 15
        login = ((login + 14) // 15) * 15
        # Round logout down to previous multiple of 15
        logout = (logout // 15) * 15
        return max(0, (logout - login) // 15)
