# Return true if every integer in [1, n] has its binary representation as a substring of s.

# Author: Kaustav Ghosh

class Solution(object):
    def queryString(self, s, n):
        for i in range(1, n + 1):
            if bin(i)[2:] not in s:
                return False
        return True
