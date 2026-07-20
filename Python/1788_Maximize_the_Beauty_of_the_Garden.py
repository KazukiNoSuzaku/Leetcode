# Author: Kaustav Ghosh
# Problem: Maximize the Beauty of the Garden (Premium)
# Approach: A valid garden starts and ends on equal-beauty flowers. For each value, its first and last occurrence bound the widest window; add the positive interior beauty (prefix sums) plus the two endpoints

class Solution(object):
    def maximumBeauty(self, flowers):
        """
        :type flowers: List[int]
        :rtype: int
        """
        # Prefix sum of only the positive beauties
        n = len(flowers)
        prefix_pos = [0] * (n + 1)
        for i, f in enumerate(flowers):
            prefix_pos[i + 1] = prefix_pos[i] + max(f, 0)

        first = {}
        best = float('-inf')
        for i, f in enumerate(flowers):
            if f in first:
                j = first[f]
                # keep both endpoints + all positive flowers strictly between them
                candidate = 2 * f + (prefix_pos[i] - prefix_pos[j + 1])
                best = max(best, candidate)
            else:
                first[f] = i
        return best
