# Author: Kaustav Ghosh
# Problem: Minimum Adjacent Swaps to Reach the Kth Smallest Number
# Approach: Apply next-permutation k times to get the target, then count the adjacent swaps to turn num into it via a greedy two-pointer (like sorting by selection)

class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        digits = list(num)

        def next_permutation(a):
            i = len(a) - 2
            while i >= 0 and a[i] >= a[i + 1]:
                i -= 1
            if i >= 0:
                j = len(a) - 1
                while a[j] <= a[i]:
                    j -= 1
                a[i], a[j] = a[j], a[i]
            a[i + 1:] = reversed(a[i + 1:])

        target = digits[:]
        for _ in range(k):
            next_permutation(target)

        # Count adjacent swaps to transform digits -> target
        original = digits[:]
        swaps = 0
        i = 0
        n = len(original)
        while i < n:
            if original[i] != target[i]:
                j = i + 1
                while original[j] != target[i]:
                    j += 1
                while j > i:
                    original[j], original[j - 1] = original[j - 1], original[j]
                    swaps += 1
                    j -= 1
            i += 1
        return swaps
