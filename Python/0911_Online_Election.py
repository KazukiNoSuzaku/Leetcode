# Query leading candidate at any time given votes and timestamps.

# Author: Kaustav Ghosh

import bisect

class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        count = {}
        leader = -1
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if leader == -1 or count[p] >= count[leader]:
                leader = p
            self.leaders.append(leader)

    def q(self, t):
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]
