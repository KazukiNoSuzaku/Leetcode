# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-jumps-to-reach-home/

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
        forbidden_set = set(forbidden)
        upper = max(max(forbidden) + a + b, x + b) + 1
        visited = set()
        visited.add((0, False))
        queue = deque([(0, 0, False)])  # position, jumps, last_was_back
        while queue:
            pos, jumps, back = queue.popleft()
            if pos == x:
                return jumps
            # Forward jump
            fwd = pos + a
            if fwd <= upper and fwd not in forbidden_set and (fwd, False) not in visited:
                visited.add((fwd, False))
                queue.append((fwd, jumps + 1, False))
            # Backward jump (only if last wasn't backward)
            if not back:
                bwd = pos - b
                if bwd >= 0 and bwd not in forbidden_set and (bwd, True) not in visited:
                    visited.add((bwd, True))
                    queue.append((bwd, jumps + 1, True))
        return -1
