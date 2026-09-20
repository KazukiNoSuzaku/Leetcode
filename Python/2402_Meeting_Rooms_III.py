# Author: Kaustav Ghosh
# Problem: Meeting Rooms III
# Approach: Take the meetings in start order with two heaps: free room numbers and busy rooms keyed by finishing time. Release every room that has finished by the meeting's start; if one is free the lowest number takes it, otherwise the meeting waits for the room that frees up first and keeps its original duration. Count each room's bookings and return the busiest, lowest number first

import heapq


class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        free = list(range(n))
        heapq.heapify(free)
        busy = []
        count = [0] * n
        for start, end in sorted(meetings):
            while busy and busy[0][0] <= start:
                heapq.heappush(free, heapq.heappop(busy)[1])
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                finish, room = heapq.heappop(busy)
                heapq.heappush(busy, (finish + end - start, room))
            count[room] += 1
        return count.index(max(count))
