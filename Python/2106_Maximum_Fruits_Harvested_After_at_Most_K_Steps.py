# Author: Kaustav Ghosh
# Problem: Maximum Fruits Harvested After at Most K Steps
# Approach: The reachable fruits form a contiguous interval [L, R]. Covering it costs (R-L) plus the shorter distance from startPos to one of its ends (go to the near end then sweep to the far end). Slide a window over the sorted fruit positions, shrinking it while the cost exceeds k, and track the best amount via prefix sums

class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        m = len(fruits)
        prefix = [0] * (m + 1)
        for idx, (_, amt) in enumerate(fruits):
            prefix[idx + 1] = prefix[idx] + amt

        def cost(i, j):
            left, right = fruits[i][0], fruits[j][0]
            return (right - left) + min(abs(startPos - left), abs(startPos - right))

        best = 0
        i = 0
        for j in range(m):
            while i <= j and cost(i, j) > k:
                i += 1
            if i <= j:
                best = max(best, prefix[j + 1] - prefix[i])
        return best
