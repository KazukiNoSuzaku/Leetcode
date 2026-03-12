# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Convert to hex, replace 0->O and 1->I, check only valid chars

class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        hex_str = hex(int(num))[2:].upper()
        hex_str = hex_str.replace('0', 'O').replace('1', 'I')
        for c in hex_str:
            if c not in 'ABCDEFIO':
                return "ERROR"
        return hex_str
