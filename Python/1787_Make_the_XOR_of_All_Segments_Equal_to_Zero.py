# Author: Kaustav Ghosh
# Problem: Make the XOR of All Segments Equal to Zero
# Approach: Two neighbouring windows of size k differ only in the element dropped and the element gained, so if both XOR to zero those two elements must be equal; the array therefore has to become periodic with period k, and the one remaining condition is that the first k values XOR to zero. That splits the indices into k residue classes, each of which must collapse to a single value, and the cost of choosing a value for a class is its size minus how often that value already occurs. The classes are then combined by a DP over the 1024 possible running XORs, with the overall best previous state carried alongside so that choosing a value absent from the class costs the full class size without looping over all 1024 options.

class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter

        LIMIT = 1024
        INF = float("inf")
        current = [INF] * LIMIT
        current[0] = 0
        best = 0
        for residue in range(k):
            counts = Counter(nums[residue::k])
            size = sum(counts.values())
            nxt = [best + size] * LIMIT
            for mask in range(LIMIT):
                if current[mask] == INF:
                    continue
                for value, seen in counts.items():
                    candidate = current[mask] + size - seen
                    if candidate < nxt[mask ^ value]:
                        nxt[mask ^ value] = candidate
            current = nxt
            best = min(current)
        return current[0]
