# Author: Kaustav Ghosh
# Problem: Minimum Skips to Arrive at Meeting On Time
# Approach: After each road but the last the clock is pushed up to the next whole hour unless that rest is skipped, so the state worth tracking is how many skips have been spent and the earliest arrival time that allows. Keeping the elapsed time multiplied by the speed turns every quantity into an integer, which matters because rounding up to the next hour becomes rounding up to the next multiple of the speed and no floating point ever enters the comparison. The table is then filled road by road, each state either resting or spending a skip, and the answer is the fewest skips whose arrival still fits inside the deadline.

class Solution(object):
    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        n = len(dist)
        INF = float("inf")
        # elapsed[j] is the earliest arrival, in kilometre units, using j skips.
        elapsed = [0] + [INF] * n
        for road in range(n):
            length = dist[road]
            last = road == n - 1
            nxt = [INF] * (n + 1)
            for skips in range(road + 1):
                if elapsed[skips] == INF:
                    continue
                travelled = elapsed[skips] + length
                rested = travelled if last else -(-travelled // speed) * speed
                if rested < nxt[skips]:
                    nxt[skips] = rested
                if travelled < nxt[skips + 1]:
                    nxt[skips + 1] = travelled
            elapsed = nxt

        deadline = hoursBefore * speed
        for skips in range(n + 1):
            if elapsed[skips] <= deadline:
                return skips
        return -1
