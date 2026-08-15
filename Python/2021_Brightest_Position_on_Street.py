# Author: Kaustav Ghosh
# Problem: Brightest Position on Street
# Approach: Each light adds brightness over [position-range, position+range]. Use a difference map (+1 at the left edge, -1 just past the right edge), sweep coordinates in order, and return the first coordinate where the running brightness reaches its maximum

from collections import defaultdict

class Solution(object):
    def brightestPosition(self, lights):
        """
        :type lights: List[List[int]]
        :rtype: int
        """
        delta = defaultdict(int)
        for pos, rng in lights:
            delta[pos - rng] += 1
            delta[pos + rng + 1] -= 1

        running = 0
        best = -1
        best_pos = 0
        for coord in sorted(delta):
            running += delta[coord]
            if running > best:
                best = running
                best_pos = coord
        return best_pos
