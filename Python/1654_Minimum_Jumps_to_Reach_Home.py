# Author: Kaustav Ghosh
# Problem: Minimum Jumps to Reach Home
# Approach: Fewest jumps over an unweighted set of moves is breadth-first search, but the state is not just the position: a backward jump may not follow another backward jump, so whether the last move went backward has to be carried along, and the same position is worth revisiting once in each of those two conditions. The other subtlety is bounding the search, since the line is infinite to the right; going beyond the target by more than one forward jump plus one backward jump can never help, because any such detour could be replaced by stopping earlier, so the search is capped there and anything above the cap or on a forbidden square is simply not expanded.

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
        limit = max([x] + forbidden) + a + b
        seen = {(0, False)}
        queue = deque([(0, False, 0)])
        while queue:
            position, came_back, jumps = queue.popleft()
            if position == x:
                return jumps
            forward = position + a
            if forward <= limit and forward not in blocked and (forward, False) not in seen:
                seen.add((forward, False))
                queue.append((forward, False, jumps + 1))
            if not came_back:
                backward = position - b
                if backward >= 0 and backward not in blocked and (backward, True) not in seen:
                    seen.add((backward, True))
                    queue.append((backward, True, jumps + 1))
        return -1
