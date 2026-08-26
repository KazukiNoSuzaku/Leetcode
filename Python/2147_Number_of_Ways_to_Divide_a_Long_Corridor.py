# Author: Kaustav Ghosh
# Problem: Number of Ways to Divide a Long Corridor
# Approach: Each section needs exactly two seats. With an even, positive seat count, a divider between consecutive seat-pairs can go in any gap from the pair's second seat up to the next pair's first seat. Multiply those gap counts

class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        if not seats or len(seats) % 2 == 1:
            return 0
        result = 1
        for i in range(2, len(seats), 2):
            result = result * (seats[i] - seats[i - 1]) % MOD
        return result
