# Author: Kaustav Ghosh
# Problem: Minimum Cost to Connect Two Groups of Points
# Approach: The second group has at most twelve points, so its coverage fits in a bitmask, and I sweep the first group one point at a time keeping the cheapest way to reach each coverage mask. Every first-group point must take at least one partner, but it may take several, which is handled by two kinds of transition into the new layer: one that starts this point's connections from the previous layer, and one that adds a further partner to the connections this point has already made in the new layer. Scanning masks upward guarantees the second kind reads a value that is already final, and a point may also re-use an already-covered partner, which is just the transition that leaves the mask unchanged.

class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        size1, size2 = len(cost), len(cost[0])
        full = (1 << size2) - 1
        INF = float('inf')

        previous = [INF] * (full + 1)
        previous[0] = 0
        for i in range(size1):
            row = cost[i]
            current = [INF] * (full + 1)
            for mask in range(full + 1):
                base = previous[mask]
                for j in range(size2):
                    target = mask | (1 << j)
                    price = row[j]
                    if base + price < current[target]:
                        current[target] = base + price
                    # Re-read rather than cache: this point may already have
                    # taken a partner earlier in this very mask.
                    if current[mask] + price < current[target]:
                        current[target] = current[mask] + price
            previous = current
        return previous[full]
