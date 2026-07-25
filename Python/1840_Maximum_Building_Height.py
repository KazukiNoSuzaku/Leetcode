# Author: Kaustav Ghosh
# Problem: Maximum Building Height
# Approach: Sort restrictions (with the fixed ends), then relax each cap forward and backward so adjacent limits differ by at most their gap. Between two consecutive restrictions the peak rises to the midpoint

class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        r = sorted(restrictions)
        r = [[1, 0]] + r + [[n, n - 1]]  # building 1 has height 0; last is unbounded

        m = len(r)
        # Forward pass: a height can rise by at most the distance from the previous
        for i in range(1, m):
            r[i][1] = min(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]))
        # Backward pass: same constraint from the right
        for i in range(m - 2, -1, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]))

        best = 0
        for i in range(1, m):
            left_id, left_h = r[i - 1]
            right_id, right_h = r[i]
            # peak between the two: (gap + hleft + hright) // 2
            peak = (right_id - left_id + left_h + right_h) // 2
            best = max(best, peak)
        return best
