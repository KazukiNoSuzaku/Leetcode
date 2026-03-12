# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Binary representation of (num + 1) minus the leading '1'

class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        return bin(num + 1)[3:]
