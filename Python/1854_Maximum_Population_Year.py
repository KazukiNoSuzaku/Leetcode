# Author: Kaustav Ghosh
# Problem: Maximum Population Year
# Approach: A person contributes to every year from birth up to but not including death, which is a range update, so instead of touching each year in the range the change is recorded only at its two ends: one more alive at the birth year, one fewer at the death year. A running total over the years then reconstructs the population at each one, and the first year to reach the maximum wins because the scan moves forward and only a strictly larger population replaces the answer.

class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        FIRST, LAST = 1950, 2050
        change = [0] * (LAST - FIRST + 2)
        for birth, death in logs:
            change[birth - FIRST] += 1
            change[death - FIRST] -= 1

        alive = 0
        most = 0
        answer = FIRST
        for offset, delta in enumerate(change):
            alive += delta
            if alive > most:
                most = alive
                answer = FIRST + offset
        return answer
