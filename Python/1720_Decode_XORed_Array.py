# Author: Kaustav Ghosh
# https://leetcode.com/problems/decode-xored-array/

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        result = [first]
        for val in encoded:
            result.append(result[-1] ^ val)
        return result
