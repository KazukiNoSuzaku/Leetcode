# Alice wins the XOR chalkboard game if XOR of all elements != 0 or count is even.

# Author: Kaustav Ghosh

class Solution(object):
    def xorGame(self, nums):
        from functools import reduce
        import operator
        return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
