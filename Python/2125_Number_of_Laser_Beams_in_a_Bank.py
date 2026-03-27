# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev = 0
        result = 0
        for row in bank:
            count = row.count('1')
            if count > 0:
                result += prev * count
                prev = count
        return result
