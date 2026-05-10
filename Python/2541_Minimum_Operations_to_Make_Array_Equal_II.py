class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # Each op adds k to one element and subtracts k from another; need diff[i] all divisible by k.
        if k == 0:
            return 0 if nums1 == nums2 else -1
        pos = neg = 0
        for a, b in zip(nums1, nums2):
            d = b - a
            if d % k != 0:
                return -1
            if d > 0:
                pos += d // k
            else:
                neg -= d // k
        return pos if pos == neg else -1
