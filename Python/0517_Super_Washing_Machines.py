# You have n super washing machines on a line. Return the minimum number of moves to make
# all washing machines have the same number of dresses. Return -1 if impossible.

# Author: Kaustav Ghosh

class Solution(object):
    def findMinMoves(self, machines):
        total = sum(machines)
        n = len(machines)
        if total % n != 0: return -1
        avg = total // n
        res = flow = 0
        for m in machines:
            flow += m - avg
            res = max(res, abs(flow), m - avg)
        return res
