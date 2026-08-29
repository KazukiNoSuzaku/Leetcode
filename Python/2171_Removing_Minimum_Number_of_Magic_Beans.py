# Author: Kaustav Ghosh
# Problem: Removing Minimum Number of Magic Beans
# Approach: All remaining non-empty bags must hold the same amount, which is best chosen as some existing bag value. Sorting, if that value is beans[i] then every bag from i onward is kept at beans[i]. Maximize kept beans (value times number of such bags); removed is total minus that

class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans.sort()
        n = len(beans)
        total = sum(beans)
        best_kept = max(beans[i] * (n - i) for i in range(n))
        return total - best_kept
