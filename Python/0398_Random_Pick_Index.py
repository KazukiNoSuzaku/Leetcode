# Given an integer array nums with possible duplicates, randomly output the index of a
# given target number. You can assume that the given target number must exist in the array.

# Author: Kaustav Ghosh

import random

class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        result = -1
        count = 0
        for i, v in enumerate(self.nums):
            if v == target:
                count += 1
                if random.randint(1, count) == 1:
                    result = i
        return result
