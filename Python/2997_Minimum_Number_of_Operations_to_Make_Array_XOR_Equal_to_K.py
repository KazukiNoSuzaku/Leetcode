from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_all = 0
        for x in nums:
            xor_all ^= x
        # Each operation flips one bit; count differing bits between current XOR and target k
        return bin(xor_all ^ k).count('1')
