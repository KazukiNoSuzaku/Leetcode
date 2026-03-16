# Author: Kaustav Ghosh
# Problem: Number of Students Doing Homework at a Given Time
# Approach: Count students where startTime <= queryTime <= endTime

class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        return sum(1 for s, e in zip(startTime, endTime) if s <= queryTime <= e)
