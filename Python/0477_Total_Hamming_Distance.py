# The Hamming distance between two integers is the number of positions at which the
# corresponding bits are different.
# Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

# Author: Kaustav Ghosh

class Solution(object):
    def totalHammingDistance(self, nums):
        total = 0
        n = len(nums)
        for bit in range(32):
            ones = sum(1 for x in nums if x & (1 << bit))
            total += ones * (n - ones)
        return total
