# Author: Kaustav Ghosh
# Problem: Count the Number of K-Big Indices
# Approach: An index needs k smaller values on each side, and the two sides are independent. Sweep right to left with a Fenwick tree over the values to mark which indices already have k smaller values to their right, then sweep left to right with a second tree and count the marked indices that also reach k on the left

class Solution(object):
    def kBigIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = max(nums)
        left_tree = [0] * (size + 1)
        right_tree = [0] * (size + 1)

        def add(tree, value):
            while value <= size:
                tree[value] += 1
                value += value & -value

        def count_below(tree, value):
            total = 0
            while value > 0:
                total += tree[value]
                value -= value & -value
            return total

        enough_right = [False] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            enough_right[i] = count_below(right_tree, nums[i] - 1) >= k
            add(right_tree, nums[i])

        big = 0
        for i, value in enumerate(nums):
            if enough_right[i] and count_below(left_tree, value - 1) >= k:
                big += 1
            add(left_tree, value)
        return big
