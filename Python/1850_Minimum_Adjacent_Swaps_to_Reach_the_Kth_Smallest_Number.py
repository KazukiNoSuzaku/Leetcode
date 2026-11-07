# Author: Kaustav Ghosh
# Problem: Minimum Adjacent Swaps to Reach the Kth Smallest Number
# Approach: The kth smallest wanted permutation is reached by applying the next-permutation step k times, which walks the arrangements in exactly the required order without enumerating or sorting any of them. Turning the original digits into that target with the fewest adjacent swaps is then a greedy sweep: for each position, the digit the target needs is pulled from the nearest place to the right that holds it, and bubbling it left costs one swap per step. Choosing the nearest copy is optimal because moving a further copy of the same digit would cross it and cost strictly more, and equal digits never need to pass each other.

class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        digits = list(num)
        n = len(digits)

        def advance():
            pivot = n - 2
            while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
                pivot -= 1
            swap = n - 1
            while digits[swap] <= digits[pivot]:
                swap -= 1
            digits[pivot], digits[swap] = digits[swap], digits[pivot]
            digits[pivot + 1:] = reversed(digits[pivot + 1:])

        for _ in range(k):
            advance()

        target = digits
        working = list(num)
        swaps = 0
        for i in range(n):
            if working[i] == target[i]:
                continue
            j = i + 1
            while working[j] != target[i]:
                j += 1
            while j > i:
                working[j], working[j - 1] = working[j - 1], working[j]
                j -= 1
                swaps += 1
        return swaps
