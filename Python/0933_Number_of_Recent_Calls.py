# Count requests in last 3000ms.

# Author: Kaustav Ghosh

from collections import deque

class RecentCounter(object):
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
