# Move all even integers to the front of the array.

# Author: Kaustav Ghosh

class Solution(object):
    def sortArrayByParity(self, nums):
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]
