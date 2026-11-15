# Author: Kaustav Ghosh
# Problem: Longest Common Subpath
# Approach: If every path shares a subpath of some length then it also shares every shorter one, so the feasible lengths form a prefix and the answer comes from a binary search over them. Testing one length means collecting, for each path, the set of its windows of that length and intersecting those sets across all the paths; the windows are represented by rolling hashes so a window costs constant work instead of its own length, and the intersection is kept as the running set so it shrinks as soon as a path disagrees. The hash is taken modulo two to the sixty-one minus one with a base drawn at random each call, which makes a collision vanishingly unlikely and cannot be provoked by a crafted input.

class Solution(object):
    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
        import random

        MOD = (1 << 61) - 1
        base = random.randrange(n + 2, MOD - 2)
        shortest = min(len(path) for path in paths)

        def windows(path, width, power):
            value = 0
            for city in path[:width]:
                value = (value * base + city + 1) % MOD
            found = {value}
            for index in range(width, len(path)):
                value = (value * base + path[index] + 1
                         - power * (path[index - width] + 1)) % MOD
                found.add(value)
            return found

        def shared(width):
            power = pow(base, width, MOD)
            common = windows(paths[0], width, power)
            for path in paths[1:]:
                if len(path) < width:
                    return False
                common &= windows(path, width, power)
                if not common:
                    return False
            return True

        low, high = 0, shortest
        while low < high:
            middle = (low + high + 1) // 2
            if shared(middle):
                low = middle
            else:
                high = middle - 1
        return low
