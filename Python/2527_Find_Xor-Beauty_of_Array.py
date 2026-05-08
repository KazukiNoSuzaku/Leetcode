from functools import reduce
from operator import xor

class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        # Each bit b survives iff the count of elements with bit b set is odd,
        # which is exactly the XOR of all elements.
        return reduce(xor, nums)
