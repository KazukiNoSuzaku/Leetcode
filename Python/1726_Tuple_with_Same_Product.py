# Author: Kaustav Ghosh
# https://leetcode.com/problems/tuple-with-same-product/

from collections import Counter

class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product_count = Counter()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product_count[nums[i] * nums[j]] += 1

        result = 0
        for count in product_count.values():
            # Each pair of pairs gives 8 tuples
            result += count * (count - 1) // 2 * 8
        return result
