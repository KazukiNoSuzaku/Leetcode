# Author: Kaustav Ghosh
# Problem: Average Salary Excluding the Minimum and Maximum Salary
# Approach: Remove min and max, compute average of the rest

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return (sum(salary) - min(salary) - max(salary)) / float(len(salary) - 2)
