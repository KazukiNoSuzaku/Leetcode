# Author: Kaustav Ghosh
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        # Pad the string if necessary
        remainder = len(s) % k
        if remainder != 0:
            s += fill * (k - remainder)
        return [s[i:i+k] for i in range(0, len(s), k)]
