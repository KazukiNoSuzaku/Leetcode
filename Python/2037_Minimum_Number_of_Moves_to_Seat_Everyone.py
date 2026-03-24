# Author: Kaustav Ghosh
# Problem 2037: Minimum Number of Moves to Seat Everyone

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        return sum(abs(s - t) for s, t in zip(seats, students))
