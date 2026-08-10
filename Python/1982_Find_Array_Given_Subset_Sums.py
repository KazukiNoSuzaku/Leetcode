# Author: Kaustav Ghosh
# Problem: Find Array Given Subset Sums
# Approach: Sort the subset sums. The gap between the two smallest is the magnitude d of some element. Pair every sum s with s+d, splitting the multiset into a "without-d" and "with-d" half. The half still containing 0 is the subset-sum set of the remaining elements: keep it and record +d if that half is the lower one, else -d. Repeat n times

from collections import Counter

class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        sums = sorted(sums)
        result = []
        for _ in range(n):
            d = sums[1] - sums[0]
            count = Counter(sums)
            without = []
            with_d = []
            for x in sums:
                if count[x] == 0:
                    continue
                count[x] -= 1
                count[x + d] -= 1
                without.append(x)
                with_d.append(x + d)
            if 0 in without:
                result.append(d)
                sums = without
            else:
                result.append(-d)
                sums = with_d
        return result
