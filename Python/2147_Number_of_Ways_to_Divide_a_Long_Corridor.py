# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # Collect positions of all seats
        seats = [i for i, c in enumerate(corridor) if c == 'S']

        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0

        result = 1
        # For each pair of seats, count the gap between
        # the end of one pair and the start of the next pair
        for i in range(2, len(seats), 2):
            gap = seats[i] - seats[i - 1]
            result = (result * gap) % MOD

        return result
