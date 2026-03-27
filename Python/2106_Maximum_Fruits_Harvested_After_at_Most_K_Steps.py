# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)
        best = 0
        curr_sum = 0
        left = 0

        for right in range(n):
            curr_sum += fruits[right][1]
            # Calculate minimum steps needed to cover fruits[left..right]
            while left <= right:
                pos_l = fruits[left][0]
                pos_r = fruits[right][0]
                # Go left first then right, or right first then left
                steps = min(
                    abs(startPos - pos_l) * 2 + abs(startPos - pos_r),
                    abs(startPos - pos_r) * 2 + abs(startPos - pos_l)
                )
                if steps <= k:
                    break
                curr_sum -= fruits[left][1]
                left += 1
            best = max(best, curr_sum)

        return best
