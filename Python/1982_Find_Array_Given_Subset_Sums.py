# Author: Kaustav Ghosh
# Problem 1982: Find Array Given Subset Sums

from collections import Counter

class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        sums.sort()
        result = []
        for _ in range(n):
            diff = sums[1] - sums[0]
            # Try both diff and -diff
            cnt = Counter(sums)
            left = []
            right = []
            for s in sums:
                if cnt[s] > 0:
                    cnt[s] -= 1
                    if cnt[s + diff] > 0:
                        cnt[s + diff] -= 1
                        left.append(s)
                        right.append(s + diff)
            # Check if 0 is in left (meaning diff is the element)
            if 0 in left:
                result.append(diff)
                sums = left
            else:
                result.append(-diff)
                sums = right
        return result
