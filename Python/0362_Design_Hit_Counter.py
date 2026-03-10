# Design a hit counter which counts the number of hits received in the past 5 minutes
# (i.e., the past 300 seconds).
# Your system should accept a timestamp parameter (in seconds granularity), and you may
# assume that calls are being made to the system in chronological order.

# Example 1:
# Input: ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
#        [[], [1], [2], [3], [4], [300], [300], [301]]
# Output: [null, null, null, null, 3, null, 4, 3]

# Constraints:
# 1 <= timestamp <= 2 * 10^9
# All the calls are being made to the system in chronological order
# At most 300 calls will be made to hit and getHits.

# Author: Kaustav Ghosh

from collections import deque

class HitCounter(object):
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)
