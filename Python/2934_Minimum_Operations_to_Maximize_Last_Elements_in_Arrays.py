from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def count(m1, m2):
            ops = 0
            for i in range(len(nums1) - 1):
                if nums1[i] <= m1 and nums2[i] <= m2:
                    continue
                elif nums1[i] <= m2 and nums2[i] <= m1:
                    ops += 1
                else:
                    return float('inf')
            return ops

        n = len(nums1)
        res = min(count(nums1[n - 1], nums2[n - 1]),
                  1 + count(nums2[n - 1], nums1[n - 1]))
        return res if res != float('inf') else -1
