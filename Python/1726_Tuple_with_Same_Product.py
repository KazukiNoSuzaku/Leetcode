# Author: Kaustav Ghosh
# Problem: Tuple with Same Product
# Approach: Count how many unordered pairs share each product; any two such pairs form 8 valid tuples, so a product with k pairs contributes 8 * C(k,2) = 4*k*(k-1)

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

        return sum(k * (k - 1) * 4 for k in products.values())
