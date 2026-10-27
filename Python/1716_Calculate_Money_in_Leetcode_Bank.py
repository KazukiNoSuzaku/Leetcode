# Author: Kaustav Ghosh
# Problem: Calculate Money in Leetcode Bank
# Approach: Each complete week deposits twenty-eight more than a base that rises by seven every week, so the complete weeks form an arithmetic series in their own right and sum in closed form rather than needing a loop. Whatever days remain begin at one more than the number of complete weeks and rise by one each day, which is a second short arithmetic series. Splitting the day count by seven gives both pieces directly.

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks, days = divmod(n, 7)
        # Complete weeks: 28, 35, 42, ... one term per week.
        full = (28 + 28 + 7 * (weeks - 1)) * weeks // 2 if weeks else 0
        # Leftover days start at weeks + 1 and climb by one.
        start = weeks + 1
        partial = (start + start + days - 1) * days // 2 if days else 0
        return full + partial
