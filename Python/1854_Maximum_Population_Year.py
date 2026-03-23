# Author: Kaustav Ghosh
# Problem 1854: Maximum Population Year

class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        delta = [0] * 101  # years 1950-2050
        for birth, death in logs:
            delta[birth - 1950] += 1
            delta[death - 1950] -= 1
        max_pop = 0
        curr = 0
        result = 1950
        for i in range(101):
            curr += delta[i]
            if curr > max_pop:
                max_pop = curr
                result = 1950 + i
        return result
