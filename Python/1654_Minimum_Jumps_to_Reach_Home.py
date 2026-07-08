# Author: Kaustav Ghosh
# Problem: Minimum Jumps to Reach Home
# Approach: BFS over states (position, came-from-backward) since two backward jumps can't chain; cap positions to max(forbidden, x) + a + b

from collections import deque

class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        blocked = set(forbidden)
        limit = max(max(forbidden, default=0), x) + a + b

        seen = {(0, False)}
        queue = deque([(0, False, 0)])  # position, arrived by backward jump, steps
        while queue:
            pos, backward, steps = queue.popleft()
            if pos == x:
                return steps

            forward = pos + a
            if forward <= limit and forward not in blocked and (forward, False) not in seen:
                seen.add((forward, False))
                queue.append((forward, False, steps + 1))

            if not backward:  # can't jump backward twice in a row
                back = pos - b
                if back >= 0 and back not in blocked and (back, True) not in seen:
                    seen.add((back, True))
                    queue.append((back, True, steps + 1))

        return -1
