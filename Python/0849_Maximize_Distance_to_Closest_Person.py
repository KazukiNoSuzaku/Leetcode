# Find the maximum distance to the nearest person when choosing a seat.

# Author: Kaustav Ghosh

class Solution(object):
    def maxDistToClosest(self, seats):
        n = len(seats)
        res = 0
        last = -1
        for i in range(n):
            if seats[i] == 1:
                res = max(res, i if last == -1 else (i - last) // 2)
                last = i
        res = max(res, n - 1 - last)
        return res
