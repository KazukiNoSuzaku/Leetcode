# Return the number of pairs (i, j) where i < j and
# (time[i] + time[j]) % 60 == 0.

# Author: Kaustav Ghosh

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        count = [0] * 60
        res = 0
        for t in time:
            rem = t % 60
            res += count[(60 - rem) % 60]
            count[rem] += 1
        return res
