# Author: Kaustav Ghosh
# Problem: Tuple with Same Product
# Approach: A valid tuple is really a pair of distinct unordered pairs sharing a product, so I tally how many pairs yield each product and then, for each product, count the ways to choose two of its pairs. Each such choice admits eight orderings of the four values, since the two pairs can be swapped and each pair can be written either way round, which is the factor of eight. Because the values are distinct, two pairs with the same product never share an element, so no choice has to be discarded.

from collections import Counter


class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        products = Counter()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                products[nums[i] * nums[j]] += 1
        total = 0
        for pairs in products.values():
            if pairs > 1:
                total += pairs * (pairs - 1) // 2 * 8
        return total
