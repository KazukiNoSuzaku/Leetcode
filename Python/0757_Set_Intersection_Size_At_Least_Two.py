# Find smallest set hitting each interval at least twice.

# Author: Kaustav Ghosh

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = []
        for lo, hi in intervals:
            count = sum(1 for x in res if lo <= x <= hi)
            if count == 0:
                res += [hi-1, hi]
            elif count == 1:
                res.append(hi if res[-1] < lo else res[-1] - 1 if res[-1] > hi else lo)
                # simplified: add the needed point
                for x in [hi, hi-1]:
                    if lo <= x <= hi and x not in res:
                        res.append(x); break
        return len(res)
