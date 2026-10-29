# Author: Kaustav Ghosh
# Problem: Maximum Subarray Sum After One Operation
# Approach: Trying the squaring at every index and running the usual maximum-subarray scan each time would be quadratic, so the two cases are carried together instead: for each position, the best subarray ending there with the squaring still unspent, which is the ordinary scan, and the best with it already spent, which either squares this very element after an unspent prefix or extends a prefix that already used it. Each state is one comparison away from the previous pair, so a single pass suffices, and because the operation is compulsory the answer takes the already-spent state into account at every position rather than only at the end.

class Solution(object):
    def maxSumAfterOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unspent = 0
        spent = 0
        best = None
        for value in nums:
            fresh_start = unspent if unspent > 0 else 0
            next_unspent = fresh_start + value
            squared_here = fresh_start + value * value
            extended = spent + value
            next_spent = squared_here if squared_here > extended else extended
            unspent, spent = next_unspent, next_spent
            if best is None or spent > best:
                best = spent
        return best
