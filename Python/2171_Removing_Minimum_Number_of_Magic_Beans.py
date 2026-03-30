# Author: Kaustav Ghosh
# Problem: 2171. Removing Minimum Number of Magic Beans
# URL: https://leetcode.com/problems/removing-minimum-number-of-magic-beans/
# Approach: Sort the array, then for each possible threshold (each element value),
#           compute total beans to remove: zero out everything below threshold and
#           reduce everything above to the threshold. Track the minimum.

class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans.sort()
        total = sum(beans)
        n = len(beans)
        min_remove = total  # worst case: remove all
        for i, val in enumerate(beans):
            # Remove all beans in bags before index i (their full count)
            # and reduce each bag from index i onward to val (remove excess)
            # Cost = prefix_sum[i] + (total - prefix_sum[i] - val * (n - i))
            #      = total - val * (n - i)
            cost = total - val * (n - i)
            if cost < min_remove:
                min_remove = cost
        return min_remove
