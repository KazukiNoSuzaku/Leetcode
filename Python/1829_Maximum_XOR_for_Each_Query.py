# Author: Kaustav Ghosh
# Problem: Maximum XOR for Each Query
# Approach: The XOR of the whole remaining array is fixed, and XOR-ing it with a chosen value under maximumBit bits is maximised by the value that flips exactly the bits the running XOR leaves at zero, which is the running XOR complemented within the mask of all ones. Removing the last element at each step just XORs it out of the running total, so the answers come out in reverse order from a single backwards pass over the array.

class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        mask = (1 << maximumBit) - 1
        running = 0
        for value in nums:
            running ^= value

        answers = []
        for value in reversed(nums):
            answers.append(running ^ mask)
            running ^= value
        return answers
