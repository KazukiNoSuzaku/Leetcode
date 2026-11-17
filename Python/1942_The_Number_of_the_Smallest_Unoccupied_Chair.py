# Author: Kaustav Ghosh
# Problem: The Number of the Smallest Unoccupied Chair
# Approach: Chairs are handed out in arrival order, and a chair becomes available the instant its occupant leaves, so I process friends sorted by arrival time and keep two heaps: one of chair numbers currently free and one of occupied chairs keyed by the time they are vacated. Before seating a friend I release every chair whose leaving time is at most this arrival, which is exactly the problem's rule that a friend leaving at the same moment frees the chair first; the smallest free chair then comes straight off the first heap. New chairs are only invented when the free heap is empty, and since at most one chair is created per friend the chair numbering matches handing out the smallest unoccupied index. I carry each friend's original index through the sort and stop on that index rather than on a time value, so nothing depends on arrival times being distinct. Sorting dominates at O(n log n).

import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        order = sorted((arrival, leaving, who)
                       for who, (arrival, leaving) in enumerate(times))

        free = []
        taken = []
        created = 0

        for arrival, leaving, who in order:
            while taken and taken[0][0] <= arrival:
                heapq.heappush(free, heapq.heappop(taken)[1])
            if free:
                chair = heapq.heappop(free)
            else:
                chair = created
                created += 1
            if who == targetFriend:
                return chair
            heapq.heappush(taken, (leaving, chair))

        return -1
