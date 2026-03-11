# Find day when two flowers bloom with exactly k empty slots between them.

# Author: Kaustav Ghosh

class Solution(object):
    def kEmptySlots(self, bulbs, k):
        n = len(bulbs)
        days = [0] * (n + 1)
        for day, pos in enumerate(bulbs, 1):
            days[pos] = day
        res = float('inf')
        lo, hi = 1, k + 2
        while hi <= n:
            valid = True
            for i in range(lo + 1, hi):
                if days[i] < days[lo] or days[i] < days[hi]:
                    lo, hi = i, i + k + 1
                    valid = False
                    break
            if valid:
                res = min(res, max(days[lo], days[hi]))
                lo, hi = hi, hi + k + 1
        return res if res != float('inf') else -1
