# Author: Kaustav Ghosh
# Problem: Find Original Array From Doubled Array
# Approach: The smallest value still unmatched can never be anyone's double, since halving it would give something smaller still, so it has to belong to the original array and must consume one copy of twice itself. Working through the distinct values in increasing order and matching every remaining copy of each against copies of its double therefore forces the only possible pairing, and a shortfall at any step proves no original array exists. Zero is the one value that pairs with itself, so its count simply has to be even and contributes half as many zeros.

class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        if len(changed) % 2 == 1:
            return []
        counts = Counter(changed)
        original = []
        for value in sorted(counts):
            remaining = counts[value]
            if remaining == 0:
                continue
            if value == 0:
                if remaining % 2 == 1:
                    return []
                original.extend([0] * (remaining // 2))
                continue
            if counts[2 * value] < remaining:
                return []
            counts[2 * value] -= remaining
            counts[value] = 0
            original.extend([value] * remaining)
        return original
