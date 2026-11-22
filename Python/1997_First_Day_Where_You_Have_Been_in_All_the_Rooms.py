# Author: Kaustav Ghosh
# Problem: First Day Where You Have Been in All the Rooms
# Approach: Because the back edge from a room always points at a room with a smaller or equal index, the rooms are first entered strictly in order, so it is enough to record the day each room is first reached. Arriving at a room for the first time leaves its visit count odd, which forces a jump back; walking forward again from there repeats exactly the work already done between the target room and the room jumped to, so the day the next room opens is twice the current day minus the day the jump target first opened, plus the two extra steps. Each room is handled with constant arithmetic under the modulus.

class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        rooms = len(nextVisit)
        first = [0] * rooms
        for room in range(rooms - 1):
            first[room + 1] = (2 * first[room] - first[nextVisit[room]] + 2) % MOD
        return first[rooms - 1]
