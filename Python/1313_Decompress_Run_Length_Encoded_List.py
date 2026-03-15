# Decompress a run-length encoded list where pairs [freq, val] expand to freq copies of val.

# Author: Kaustav Ghosh

class Solution(object):
    def decompressRLElist(self, nums):
        res = []
        for i in range(0, len(nums), 2):
            res.extend([nums[i+1]] * nums[i])
        return res
