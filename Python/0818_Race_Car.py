# Find minimum instructions to reach target position using accelerate and reverse.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def racecar(self, target):
        q = deque([(0, 1, 0)])
        visited = {(0, 1)}
        while q:
            pos, speed, steps = q.popleft()
            for npos, nspeed in [(pos + speed, speed * 2), (pos, -1 if speed > 0 else 1)]:
                if npos == target: return steps + 1
                if (npos, nspeed) not in visited and -target <= npos <= 2 * target:
                    visited.add((npos, nspeed))
                    q.append((npos, nspeed, steps + 1))
        return -1
