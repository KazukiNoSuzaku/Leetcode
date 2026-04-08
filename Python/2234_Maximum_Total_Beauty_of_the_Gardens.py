# Author: Kaustav Ghosh
# Problem: 2234. Maximum Total Beauty of the Gardens
# URL: https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/
# Difficulty: Hard
#
# Approach:
# Sort gardens. Use a suffix decision: the last j gardens (largest) can be
# completed to target. For the remaining gardens, maximize the minimum using
# prefix sums and binary search. Iterate over how many gardens to complete
# and find the best combination of full + partial beauty.

class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        :type flowers: List[int]
        :type newFlowers: int
        :type target: int
        :type full: int
        :type partial: int
        :rtype: int
        """
        n = len(flowers)
        flowers = [min(f, target) for f in flowers]
        flowers.sort()

        # If all gardens can be completed
        if flowers[0] == target:
            return n * full

        # prefix[i] = sum of flowers[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + flowers[i]

        # Cost to complete the last j gardens (indices n-j .. n-1) to target
        # We iterate j from 0 to n
        # cost_complete[j] = sum of (target - flowers[i]) for i in [n-j, n-1]
        # Precompute the cost to complete the rightmost j gardens
        cost = 0
        # max_complete[j] = cost to fill last j gardens to target
        max_complete = [0] * (n + 1)
        for j in range(1, n + 1):
            cost += target - flowers[n - j]
            max_complete[j] = cost

        best = 0
        # For each number of completed gardens j (0..n), check feasibility
        for j in range(n + 1):
            remaining = newFlowers - max_complete[j]
            if remaining < 0:
                break
            if j == n:
                best = max(best, n * full)
                break
            # Now we have n-j incomplete gardens: flowers[0..n-j-1]
            # We want to maximize the minimum among them using 'remaining' flowers
            # Binary search on the minimum value m
            lo, hi = flowers[0], target - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                # Cost to raise all flowers[0..n-j-1] to at least mid
                # Find first index where flowers[idx] >= mid using binary search
                left, right = 0, n - j
                while left < right:
                    m2 = (left + right) // 2
                    if flowers[m2] >= mid:
                        right = m2
                    else:
                        left = m2 + 1
                # left = first index with flowers[idx] >= mid
                # Cost = mid * left - prefix[left]
                need = mid * left - prefix[left]
                if need <= remaining:
                    lo = mid
                else:
                    hi = mid - 1
            beauty = j * full + lo * partial
            best = max(best, beauty)

        return best
