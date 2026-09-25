# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Make Arrays Similar
# Approach: An operation moves 2 from one element to another, so each element keeps its parity and odds must match odds, evens evens. Sorting each parity class and pairing them in order is optimal, and since every operation covers 2 units of a shortfall, the answer is the total shortfall divided by 2

class Solution(object):
    def makeSimilar(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        operations = 0
        for parity in (0, 1):
            have = sorted(x for x in nums if x % 2 == parity)
            want = sorted(x for x in target if x % 2 == parity)
            operations += sum(max(w - h, 0) for h, w in zip(have, want))
        return operations // 2
