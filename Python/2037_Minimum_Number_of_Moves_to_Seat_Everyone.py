# Author: Kaustav Ghosh
# Problem: Minimum Number of Moves to Seat Everyone
# Approach: Sorting both seats and students and pairing them in order minimizes total distance; sum the absolute differences

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        return sum(abs(a - b) for a, b in zip(sorted(seats), sorted(students)))
