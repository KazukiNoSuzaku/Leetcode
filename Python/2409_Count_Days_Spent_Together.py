# Author: Kaustav Ghosh
# Problem: Count Days Spent Together
# Approach: The year is not a leap year, so turn each MM-DD date into its day of the year with a prefix sum of month lengths. The stay overlaps between the later arrival and the earlier departure, which is that many days inclusive, or none if the range is empty

class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        before = [0]
        for length in months:
            before.append(before[-1] + length)

        def day_of_year(date):
            return before[int(date[:2]) - 1] + int(date[3:])

        start = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        end = min(day_of_year(leaveAlice), day_of_year(leaveBob))
        return max(0, end - start + 1)
