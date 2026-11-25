# Author: Kaustav Ghosh
# Problem: Minimum Number of Moves to Seat Everyone
# Approach: Pairing the students and seats in sorted order is optimal, because if a nearer student were assigned the further seat and vice versa, swapping those two assignments never increases the combined distance and often shortens it. So both lists are sorted and matched position by position, and the total cost is the sum of the absolute gaps between the paired values. Repeated positions need no special handling, since sorting places identical values adjacent and the pairing remains valid.

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        return sum(abs(seat - student)
                   for seat, student in zip(sorted(seats), sorted(students)))
