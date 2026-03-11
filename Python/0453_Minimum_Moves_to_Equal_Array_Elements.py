# Given an integer array nums of size n, return the minimum number of moves required to
# make all array elements equal, where a move is incrementing n-1 elements by 1.
# Incrementing n-1 is equivalent to decrementing 1; so answer is sum(nums) - n*min(nums).

# Author: Kaustav Ghosh

class Solution(object):
    def minMoves(self, nums):
        return sum(nums) - min(nums) * len(nums)
