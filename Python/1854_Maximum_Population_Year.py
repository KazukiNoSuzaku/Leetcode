# Author: Kaustav Ghosh
# Problem: Maximum Population Year
# Approach: Difference array over years (birth adds, death removes); sweep the prefix sum and keep the earliest year with the peak population

class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        delta = [0] * 2051
        for birth, death in logs:
            delta[birth] += 1
            delta[death] -= 1

        best_year = 1950
        best_pop = 0
        running = 0
        for year in range(1950, 2051):
            running += delta[year]
            if running > best_pop:
                best_pop = running
                best_year = year
        return best_year
