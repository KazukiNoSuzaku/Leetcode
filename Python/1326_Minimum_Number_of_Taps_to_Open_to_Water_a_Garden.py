# Garden from 0 to n. Each tap at position i covers [i-ranges[i], i+ranges[i]].
# Return minimum taps to water the whole garden, or -1 if impossible.

# Author: Kaustav Ghosh

class Solution(object):
    def minTaps(self, n, ranges):
        # Convert to interval cover problem
        max_reach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            max_reach[left] = max(max_reach[left], i + r)
        taps = cur_end = far = 0
        for i in range(n):
            far = max(far, max_reach[i])
            if i == cur_end:
                if far == cur_end:
                    return -1
                cur_end = far
                taps += 1
        return taps
