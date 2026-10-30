# Author: Kaustav Ghosh
# Problem: Maximum Number of Events That Can Be Attended II
# Approach: Sorting the events by end day makes the choice sequential: for each event, either skip it or take it and continue from the last event that finishes strictly before it begins. That predecessor never changes, so it is located once per event by binary search over the sorted end days rather than inside the table. The table itself is indexed by how many events may still be attended and how far through the list we are, and since each layer reads only the layer with one fewer attendance left, two rolling rows replace the full grid; the total work is the number of events times the attendance cap, which the constraints bound directly.

from bisect import bisect_left


class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        ordered = sorted(events, key=lambda event: event[1])
        n = len(ordered)
        ends = [event[1] for event in ordered]
        starts = [event[0] for event in ordered]
        values = [event[2] for event in ordered]

        # Last event finishing strictly before this one starts.
        previous = [bisect_left(ends, starts[i]) for i in range(n)]

        fewer = [0] * (n + 1)
        for _attendances in range(k):
            current = [0] * (n + 1)
            for i in range(n):
                skip = current[i]
                take = fewer[previous[i]] + values[i]
                current[i + 1] = skip if skip > take else take
            fewer = current
        return fewer[n]
