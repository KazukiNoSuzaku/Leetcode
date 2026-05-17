from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        # Each element can become any value congruent to it mod value.
        # Count remainders; greedily assign 0,1,2,... using available remainder slots.
        rem_count = Counter(x % value for x in nums)
        mex = 0
        while rem_count[mex % value] > 0:
            rem_count[mex % value] -= 1
            mex += 1
        return mex
